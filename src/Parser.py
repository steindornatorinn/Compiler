from Token import *
import sys
class Parser(object):
    '''A parser for our programming language'''
    #Current token
    token = None
    def __init__(self, lexer):
        '''Initialization function, takes a lexical analyzer as a argument'''
        self.lexer = lexer

    def parse(self):
        '''A parser parses'''
        self.token = self.lexer.nextToken()
        self.statements()

    def statements(self):
        '''Parse statements'''
        while True:
            #If we recieve a end token, stop
            if self.accept(Token_codes.END):
                sys.exit(0)
            #Else parse a single statment
            else:
                self.statement()

    def statement(self):
        '''Parse a single statement'''
        #statement -> Print ID | expression
        temp = self.token.lexeme
        if self.accept(Token_codes.PRINT):
            temp = self.token.lexeme
            self.expect(Token_codes.ID)
            print "PUSH " + temp
            print "PRINT"
        elif self.accept(Token_codes.ID):
            print "PUSH " + temp
            self.expect(Token_codes.ASSIGN)
            self.expression()
            print "ASSIGN"
        #all statements must be ended with a semicolon
        self.expect(Token_codes.SEMICOL)

    def expression(self):
        '''Parse a single expression'''
        #expression -> term | term + expression | term - expression
        self.term()
        if(self.accept(Token_codes.ADD)):
            self.expression()
            print "ADD"
        if(self.accept(Token_codes.SUB)):
            self.expression()
            print "SUB"

    def term(self):
        '''Parse a single term'''
        #term -> factor| factor * term
        self.factor()
        if(self.accept(Token_codes.MULT)):
            self.term()
            print "MULT"

    def factor(self):
        '''Parse a single factor'''
        # factor -> ID | INT | (EXPRESSION)
        temp = self.token.lexeme
        if(self.accept(Token_codes.ID)):
            print "PUSH " + temp
        elif(self.accept(Token_codes.INT)):
            print "PUSH " + temp
        elif(self.accept(Token_codes.LPAREN)):
            self.expression()
            self.expect(Token_codes.RPAREN)
        else:
            self.error("Syntax error!")

    def error(self, message):
        '''Print a error message and exit'''
        print message
        sys.exit(0)

    def accept(self, token):
        '''If the current token is the same as the passed one, return true and get the next one'''
        if self.token.token_code == token:
            self.token = self.lexer.nextToken()
            if self.token == Token_codes.ERROR: 
                self.error("Lexical Error")
            return True
        else:
            return False

    def expect(self, token):
        '''Ensure the current token is the same one that we expect it to be'''
        accepted = self.accept(token)
        if accepted:
            return True
        else:
            self.error("Unexpected token: \n" + str(self.token))
            return False
    

