import sys
# Stack class taken from http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
		 

class Interpreter:
    s = Stack()
    assignDict = {}
    checkpush = False
    # push function check if op exists in dictionary used for variable
    def push(self, op):
        if op in self.assignDict:
            op = self.assignDict[op]
        self.s.push(op)
   
    def add(self):
        number = self.s.pop()
        number2 = self.s.pop()
        sums = number + number2
        self.s.push(sums)
    
    def sub(self):
        number = self.s.pop()
        number2 = self.s.pop()
        sums = number2 - number
        self.s.push(sums)
    
    def mult(self):
        number = self.s.pop()
        number2 = self.s.pop()
        sums = number * number2
        self.s.push(sums)
    
    def assign(self):
        number = self.s.pop()
        var = self.s.pop()
        self.assignDict[var] = number    
        self.s.push(number)
    
    def print(self):
        print (self.s.peek())
    # stdin function that spilt on every word and check every word for keyword
    def read_in(self):
        for lines in sys.stdin:
            lines = lines.strip()
            words = lines.split()
            for word in words:
                if (self.checkpush):
                    if(word.isdigit()):
                        self.push(int(word))
                    else:
                        self.push(word)
                    self.checkpush = False
                elif (word == "PUSH"):
                    self.checkpush = True
                else:
                    self.checkWordForOp(word)
    # check word for op keyword
    def checkWordForOp(self,word):
        if(word == "ADD"):
            if (self.checkStackForTwo()):
                self.add()
            else:
                print("Error for operator: ADD");
                sys.exit(0)
        elif(word == "MULT"):
            if (self.checkStackForTwo()):
                self.mult()
            else:
                print("Error for operator: MULT");
                sys.exit(0)
        elif(word == "SUB"):
            if (self.checkStackForTwo()):
                self.sub()
            else:
                print("Error for operator: SUB");
                sys.exit(0)
        elif(word == "ASSIGN"):
            if (self.checkStackForTwo()):
                self.assign()
            else:
                print("Error for operator: ASSIGN");
                sys.exit(0)
        elif(word == "PRINT"):
            if (self.s.size() > 0) :
                self.print()
            else:
                print("Error for operator: PRINT");
                sys.exit(0)
        else:
            print("Error for operator: "+word);
            sys.exit(0)
    # check if stack has 2 or more items
    def checkStackForTwo(self):
        if(self.s.size() > 1):
            return True
        else:
            return False

def main():
    lines = Interpreter().read_in()

if __name__ == '__main__':
    main()
