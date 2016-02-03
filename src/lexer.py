from token import Token_codes
from token import Token
from instream import Instream
import sys
class Lexer(object):
    '''A lexical analyzer for our language'''
    stdin = Instream()

    def nextToken(self): 
        '''Fetch the next token from stdin'''
        nextchar = self.stdin.getvisible()
        result = ""
        #Search throuch stdin untill we find a token or encounter a EOF character
        while(True):
            if nextchar == '+':
                return Token(Token_codes.ADD)
            elif nextchar == '-':
                return Token(Token_codes.SUB) 
            elif nextchar == '=':
                return Token(Token_codes.ASSIGN)
            elif nextchar == '*':
                return Token(Token_codes.MULT)
            elif nextchar == ')':
                return Token(Token_codes.RPAREN)
            elif nextchar == '(':
                return Token(Token_codes.LPAREN)
            elif nextchar == ';':
                return Token(Token_codes.SEMICOL)
            elif nextchar.isalnum():
                #If the first character is a letter this is a id
                if nextchar.isalpha():
                    #loop through untill we find all the characters in the string
                    while nextchar.isalnum():
                        result += nextchar
                        nextchar = self.stdin.getvisible()
                        if result == "end":
                            self.stdin.ungetchar(nextchar)
                            return Token(Token_codes.END)
                        if result == "print":
                            self.stdin.ungetchar(nextchar)
                            return Token(Token_codes.PRINT)
                    #return the additional character we stole
                    self.stdin.ungetchar(nextchar)
                    #Keywords
                    return Token(Token_codes.ID, result)
                #If the first character is a digit this is a integer
                else:
                    error = False
                    #loop through untill we find all the characters in the string
                    while nextchar.isalnum():
                        result += nextchar
                        #If there are letters in our integer, return a error
                        if nextchar.isalpha():
                           error = True
                        nextchar = self.stdin.getvisible()
                    #return the additional character we stole
                    self.stdin.ungetchar(nextchar)
                    #Return a error if one occurred
                    if error:
                        return Token(Token_codes.ERROR)
                    else:
                        return Token(Token_codes.ID, result)
            else:
                #Symbol not in our syntax
                if nextchar == '': 
                   sys.exit(0)
                return Token(Token_codes.ERROR)
