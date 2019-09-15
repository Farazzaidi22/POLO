import Error
#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
ALPHABETS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'

KeyWord = ['int', 'float', 'string', 'char', 'bool', 'var', 'if', 'else', 'for', 'while', 'class', 'public', 'private', 
            'protected', 'virtual', 'override', 'static', 'enum', 'return', 'break', 'continue','new', 'meth']

def Search_For_KeyWord(n):
    for i in range(len(KeyWord)):
        if KeyWord[i] == n:
            return True
    return False

###################
# TOKEN
###################

TT_KW       = 'KeyWord'
TT_ID       = 'Variable'
TT_STRING   = "STRING"

TT_INT		= 'INT_Number'
TT_FLOAT    = 'FLOAT_Number'
TT_VARIABLE = 'Variable'

TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_MOD      = 'Mod'


TT_EqualsTo          = 'Equals'
TT_PlusEquals        = 'PlusEquals'
TT_MinEquals         = 'MinEquals'
TT_MulEquals         = 'MulEquals'
TT_DivEquals         = 'DivEquals'
TT_ModEquals         = 'ModEquals'


TT_GreaterThan      = 'Greater'
TT_LessThan         = 'Lesser'
TT_GreaterEqual     = 'GreaterThanEqualTo'
TT_LesserEqual      = 'LesserThanEqualTo'
TT_DoubleEquals     = 'DoubleEquals'
TT_NotEquals        = 'NotEqualsTo'
TT_NOT              = 'NOT'

TT_LPARENR   = 'LPARENRound'
TT_RPARENR   = 'RPARENRound'
TT_LPARENC   = 'LPARENCurly'
TT_RPARENC   = 'RPARENCurly'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

#to return value and type of the input
    # def __reprint__(self):
    #     if (self.value):
    #         return f'{self.type}:{self.value}'
    #     else:
    #         return f'{self.type}'


#######################################
# LEXER
#######################################

class Lexer:
    #constructor
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    #For moving char to char
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if(self.pos < len(self.text)) else None
        
    def make_Number(self):
        num_string = '' #to save our digits
        dot_count  = 0   #To keep track of decimal

        while self.current_char != None and self.current_char in DIGITS + '.':
            if (self.current_char == '.'):
                if (dot_count == 1):
                    break
                dot_count = dot_count + 1
                num_string += '.'
            else:
                num_string += self.current_char
            self.advance()
        

        if (dot_count == 0):
            return Token(TT_INT, int(num_string))
        else:
            return Token(TT_FLOAT, float(num_string))
    
    def make_variable(self):
        var_str = ''

        while self.current_char != None and self.current_char in ALPHABETS:
            var_str += self.current_char
            self.advance()
        
        x = Search_For_KeyWord(var_str)
        if x == True:
            return Token(TT_KW, (var_str))
        else:
            return Token(TT_ID, (var_str))
    
    def make_String(self):
        str_str = ''
        quot_count = 0

        while self.current_char != None and self.current_char in ALPHABETS + '\"':
            if self.current_char == '\"':
                if quot_count == 1: break
                quot_count += 1
            else:
                str_str += self.current_char
            self.advance()
                
        return Token(TT_STRING, str_str)


    def make_tokens(self):
        tokens = []

        while(self.current_char != None):
            
    #to ignore spaces and tabs
            if(self.current_char in " \t"):
                self.advance()
            
    #For Numbers
            elif(self.current_char in DIGITS):
                tokens.append(self.make_Number())
    
    #For keywords and variables
            elif(self.current_char in ALPHABETS):
                tokens.append(self.make_variable())
    #For strings
            elif self.current_char == '\"' :
                tokens.append(self.make_String())
            
    #For Arithematic Operators and Asssignment Operators
            elif(self.current_char == "+"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_PlusEquals))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_PLUS))
                    self.advance()
            
            elif(self.current_char == "-"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_MinEquals))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_MINUS))
                    self.advance()
            
            elif(self.current_char == "*"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_MulEquals))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_MUL))
                    self.advance()
            
            elif(self.current_char == "/"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_DivEquals))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_DIV))
                    self.advance()
            
            elif(self.current_char == "%"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_ModEquals))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_MOD))
                    self.advance()

    #Relational Operators 
            elif(self.current_char == "="):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_DoubleEquals))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_EqualsTo))
                    self.advance()

            elif(self.current_char == ">"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_GreaterEqual))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_GreaterThan))
                    self.advance()
            
            elif(self.current_char == "<"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_LesserEqual))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_LessThan))
                    self.advance()
            
            elif(self.current_char == "!"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_NotEquals))
                    self.advance()
                else:
                    self.current_char = temp
                    tokens.append(Token(TT_NOT))
                    self.advance()
    #Braces
            elif self.current_char == '(':
                tokens.append(Token(TT_LPARENR))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPARENR))
                self.advance()
            elif self.current_char == '{':
                tokens.append(Token(TT_LPARENC))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TT_RPARENC))
                self.advance()
            
            else:
                char = self.current_char
                self.advance()
                return [], Error.IllegalCharError("'" + char + "'")

        return tokens, None

#######################################
# RUN
#######################################

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    return tokens, error

            


