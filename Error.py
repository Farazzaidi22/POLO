# from strings_with_arrows import *

class Error:
    def __init__(self,pos_start, pos_end, error_name, details):
        self.pos_start  = pos_start
        self.pos_end    = pos_end
        self.error_name = error_name
        self.details    = details
    
    #create errror as a string
    def as_string(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f' at line{self.pos_start.ln + 1}'
        # result += '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result
        
class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'Invalid Syntax', details)

#inheritance (error = superclass) It allows us to call the
#constructor(can be any other fun as well) of the base class
