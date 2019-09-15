class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    
    #create errror as a string
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

#inheritance (error = superclass) It allows us to call the
#constructor(can be any other fun as well) of the base class
