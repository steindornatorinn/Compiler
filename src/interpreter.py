import stack
class Interpreter:
	s = stack.Stack()
    assign = {}
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
        sums = number - number2
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
	def read_in():
	    for lines in sys.stdin:
		lines = lines.strip()
        words = lines.split()
        for word in words:
            print(word)
	def checkStackForTwo(self):
		if(self.s.size() > 2):
			return True
		else
			return False
	#print("Error for operator: add");
	#print("Error for operator: sub");
	#print("Error for operator: mult");
	#print("Error for operator: assign");
	#print("Error for operator: print");
	#http://albertech.blogspot.is/2015/02/either-read-from-stdin-or-prompt-user.html
def main():
	lines = read_in()

if __name__ == '__main__':
    main()