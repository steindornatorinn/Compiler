import lexer
import parser
class Compiler(object):
    lexer = lexer.Lexer()
    parser = parser.Parser(lexer)
    def main(self):
        self.parser.parse()

if __name__ == "__main__":
    compiler = Compiler() 
    compiler.main()
