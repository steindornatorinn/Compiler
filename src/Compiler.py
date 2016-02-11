import Lexer
import Parser
class Compiler(object):
    lexer = Lexer.Lexer()
    parser = Parser.Parser(lexer)
    def main(self):
        self.parser.parse()

if __name__ == "__main__":
    compiler = Compiler() 
    compiler.main()
