import compiler

class main:
    c = compiler.Compiler()
    c.Push("var")
    c.Push(2)
    c.Assign()
    c.Push(5)
    c.Add()
    c.Print()
    
