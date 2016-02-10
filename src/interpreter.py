import sys
class Interpreter:
    s = stack.Stack()
    assign = {}
    checkpush = False
    def Push(self, op):
        if op in self.assign:
            op = self.assign[op]
        self.s.push(op)
    def Add(self):
        number = self.s.pop()
        number2 = self.s.pop()
        sums = number + number2
        self.s.push(sums)
    def Sub(self):
        number = self.s.pop()
        number2 = self.s.pop()
        sums = number2 - number
        self.s.push(sums)
    def Mult(self):
        number = self.s.pop()
        number2 = self.s.pop()
        sums = number * number2
        self.s.push(sums)
    def Assign(self):
        number = self.s.pop()
        var = self.s.pop()
        self.assign[var] = number    
        self.s.push(number)
    def Print(self):
        print (self.s.peek())
    def read_in(self):
        for lines in sys.stdin:
            lines = lines.strip()
            words = lines.split()
            for word in words:
                if (self.checkpush):
                    if(word.isdigit()):
                        self.Push(int(word))
                    else:
                        self.Push(word)
                    self.checkpush = False
                elif (word == "PUSH"):
                    self.checkpush = True
                else:
                    self.checkWordForOp(word)
    def checkWordForOp(self,word):
        if(word == "ADD"):
            if (self.checkStackForTwo()):
                self.Add()
            else:
                print("Error for operator: ADD");
                sys.exit(0)
        if(word == "MULT"):
            if (self.checkStackForTwo()):
                self.Mult()
            else:
                print("Error for operator: MULT");
                sys.exit(0)
        if(word == "SUB"):
            if (self.checkStackForTwo()):
                self.Sub()
            else:
                print("Error for operator: SUB");
                sys.exit(0)
        if(word == "ASSIGN"):
            if (self.checkStackForTwo()):
                self.Assign()
            else:
                print("Error for operator: ASSIGN");
                sys.exit(0)
        if(word == "PRINT"):
            if (self.s.size() > 0) :
                self.Print()
            else:
                print("Error for operator: PRINT");
                sys.exit(0)
    def checkStackForTwo(self):
        if(self.s.size() > 1):
            return True
        else:
            return False
			
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
			
def main():
    lines = Interpreter().read_in()

if __name__ == '__main__':
    main()
