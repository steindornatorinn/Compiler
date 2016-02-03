from array import *
import stack
class Compiler:
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
        print self.s.peek()
