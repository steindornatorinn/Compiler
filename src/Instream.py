import sys
class Instream(object):
    '''A extremely barebones wrapper for the input stream'''
    backlog = []
    
    def getvisible(self):
        '''Get a single non-whitespace character from the input stream'''
        while True:
            result = self.getchar() 
            if result != ' ' and result != '\n':
                return result

    def getchar(self):
        '''Get a single character from the stream'''
        if self.backlog == []:
            nextchar = sys.stdin.read(1)
            if nextchar != None:
                return nextchar
            sys.exit(0)
        else:
            result = self.backlog[-1] 
            del self.backlog[-1]
            return result

    def ungetchar(self, char):
        '''Return a single character to the front of the stream'''
        self.backlog.append(char)
