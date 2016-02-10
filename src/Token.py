class Token_codes(object):
    '''Enumeration class for token codes'''
    ID, ASSIGN, SEMICOL, INT, ADD, SUB, MULT, LPAREN, RPAREN, PRINT, END, ERROR = range(1,13)

class Token(object):
    '''Represents a single token in our programming language'''
    lexeme = ""
    token_code = 0 

    def __init__(self, token_code, lexeme = ""):
        self.lexeme = lexeme
        self.token_code = token_code

    def __repr__(self):
        representation = "token with token code: " + str(self.token_code) 
        if self.lexeme != "":
            representation += "\nwith lexeme: " + self.lexeme 
        return representation
