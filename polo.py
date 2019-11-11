import Error
import Position
import Parser
import strings_with_arrows

#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
ALPHABETS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
SPECIALCHARACTERS ='!@#$%^&|~`+-*/\\='

KeyWord             = ['static', 'enum', 'continue']
DataType            = ['int', 'float', 'string', 'char', 'bool', 'var']
# loops               = ['for', 'while']
# conditional         = ['if', 'else']
booll               = ['True', 'False']
Access_Modifiers    = ['public', 'private','protected']
Type_Modifers       = ['virtual','override']
Logical_Operator    = ['and', 'or', 'not']
puntuators          = [';', ',', '\n', ':', '[', ']', '{', '}', '(', ')', '.']

# def Search_For_KeyWord(n):
#     for i in range(len(KeyWord)):
#         if KeyWord[i] == n:
#             return True
#     return False

###################
# TOKEN
###################

TT_CLASS                 = 'Class'
TT_ENDMARKER             = 'EndMarker'
TT_METH                  = 'Meth'
# TT_MAIN                  = 'main'
TT_NEW                   = 'new'
TT_RET                   = 'return' 
TT_BREAK                 = 'break'
TT_IF                    = 'if'
TT_ELSE                  = 'else'
TT_FOR                   = 'for'
TT_IN                    = 'in'
TT_RANGE                 = 'range'
TT_WHILE                 = 'while'


TT_ACESSOR               = 'Acessor'
TT_SCOPERESOLUTION       = 'ScopeResolution'
TT_INHERITANCE_INITIATOR = 'inheritant initiator'

TT_KW           = 'KeyWord'
TT_DT           = 'DataType'
TT_lOOPS        = 'Loop'
TT_CONDTIONAL   = 'conditional'
TT_ACESSORMOD   = 'Access_Modifiers'
TT_TYPEMOD      = 'Type_Modifers'
TT_LOGICALOP    = 'Logical_Operator'
TT_ID           = 'Variable'


TT_STRING   = "STRING"
TT_CHAR     = 'CHAR'
TT_BOOL     = 'Boolean'

TT_INT		= 'INT_Number'
TT_FLOAT    = 'FLOAT_Number'

TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_MOD      = 'Mod'


TT_ASSIGNMENTOP        = 'AssignmentOperator'
# TT_EqualsTo          = 'Equals'
# TT_PlusEquals        = 'PlusEquals'
# TT_MinEquals         = 'MinEquals'
# TT_MulEquals         = 'MulEquals'
# TT_DivEquals         = 'DivEquals'
# TT_ModEquals         = 'ModEquals'


TT_RELATIONALOP     = 'RelationalOperator'
# TT_GreaterThan      = 'Greater'
# TT_LessThan         = 'Lesser'
# TT_GreaterEqual     = 'GreaterThanEqualTo'
# TT_LesserEqual      = 'LesserThanEqualTo'
# TT_DoubleEquals     = 'DoubleEquals'
# TT_NotEquals        = 'NotEqualsTo'
TT_NOT              = 'NOT'

TT_LPARENR   = 'LPARENRound'
TT_RPARENR   = 'RPARENRound'

TT_LPARENC   = 'LPARENCurly'
TT_RPARENC   = 'RPARENCurly'

TT_LPARENS   = 'LPARENSquare'
TT_RPARENS   = 'RPARENSquare'

TT_TERMINATOR = 'Terminator'
TT_SEPARATOR  = 'Separator'


class Token:
    def __init__(self, type_, value=None, pos_start = None, pos_end = None):
        self.type   = type_
        self.value  = value
        
        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance(pos_start)

        if pos_end:
            self.pos_end = pos_end

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

#to return value and type of the input
    def __repr__(self):
        if (self.value):
            return f'{self.type}:{self.value}'
        else:
            return f'{self.type}'


#######################################
# LEXER
#######################################

class Lexer:
    #constructor
    def __init__(self, text):
        self.text = text
        self.pos = Position.Position(-1,0,-1)
        self.current_char = None
        self.advance()

    #For moving char to char
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if(self.pos.idx < len(self.text)) else None

    def make_Number(self):
        num_string = '' #to save our digits
        dot_count  = 0   #To keep track of decimal
        pos_start = self.pos.copy()

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
            return Token(TT_INT, int(num_string),pos_start, self.pos)
        else:
            return Token(TT_FLOAT, float(num_string), pos_start, self.pos)
    
    def make_variable(self):
        var_str = ''

        while self.current_char != None and self.current_char in ALPHABETS + DIGITS:
            var_str += self.current_char
            self.advance()
        
        if(var_str in KeyWord):
            return Token(TT_KW, var_str)

        elif(var_str == 'class'):
            return Token(TT_CLASS, var_str)
        
        elif(var_str == 'meth'):
            return Token(TT_METH, var_str)
        
        # elif(var_str == 'main'):
        #     return Token(TT_MAIN, var_str)
        
        elif(var_str == 'new'):
            return Token(TT_NEW, var_str)
        
        elif(var_str == 'return'):
            return Token(TT_RET, var_str)
        
        elif(var_str == 'break'):
            return Token(TT_BREAK, var_str)
        
        elif(var_str == 'if'):
            return Token(TT_IF, var_str)
        
        elif(var_str == 'else'):
            return Token(TT_ELSE, var_str)
        
        elif(var_str == 'for'):
            return Token(TT_FOR, var_str)
        
        elif(var_str == 'in'):
            return Token(TT_IN, var_str)
        
        elif(var_str == 'range'):
            return Token(TT_RANGE, var_str)
        
        elif(var_str == 'while'):
            return Token(TT_WHILE, var_str)
        
        elif(var_str in DataType):
            return Token(TT_DT, var_str)
        
        elif(var_str in booll):
            return Token(TT_BOOL, var_str)
        
        elif(var_str in Access_Modifiers):
            return Token(TT_ACESSORMOD, var_str)
        
        elif(var_str in Type_Modifers):
            return Token(TT_TYPEMOD, var_str)
        
        elif(var_str in Logical_Operator):
            return Token(TT_LOGICALOP, var_str)
        
        else:
            return Token(TT_ID, var_str)


    def make_String(self):
        str_str = ''
        quot_count = 0

        while self.current_char != None and self.current_char in ALPHABETS + '\"' + ' \t'+ '\\' + DIGITS + SPECIALCHARACTERS:
            if self.current_char == '\"':
                if quot_count == 0: 
                    quot_count += 1
                    self.advance()
                    if quot_count == 1:
                        return Token(TT_STRING, str_str)

            else:
                str_str += self.current_char
            self.advance()
    
    def make_char(self):
        char_str= ''
        quot_count = 0

        while self.current_char != None and self.current_char in ALPHABETS + '\'' + ' \t' + DIGITS + SPECIALCHARACTERS:
            if self.current_char == '\'':
                if quot_count == 0: 
                    quot_count += 1
                    self.advance()
                    if len(char_str) == 1 and quot_count == 1:
                        return Token(TT_CHAR, char_str)
                    elif len(char_str) > 1:
                        print("error")

            else:
                char_str += self.current_char
            self.advance()
    

    def skip_comment(self):
        self.advance()

        while self.current_char != '\n':
            self.advance()
        
        self.advance()
        

    def make_tokens(self):
        tokens = []

        while(self.current_char != None):
            
    #to ignore spaces and tabs
            if(self.current_char in " \t"):
                self.advance()
    
    #For change of line
            elif(self.current_char in "\n"):
                # tokens.append(Token(TT_TERMINATOR))
                self.advance()
    
    #For terminal
            elif(self.current_char in ";"):
                tokens.append(Token(TT_TERMINATOR))
                self.advance()
    #For terminal
            elif(self.current_char in ","):
                tokens.append(Token(TT_SEPARATOR))
                self.advance()
    
    #For comments (single line for now)
            elif(self.current_char in "#"):
                self.skip_comment()
                self.advance()
            
    #For Numbers
            elif(self.current_char in DIGITS):
                tokens.append(self.make_Number())              
    
    #For keywords and variables
            elif(self.current_char in ALPHABETS):
                tokens.append(self.make_variable())
                
    #For strings
            elif self.current_char == '\"':
                self.advance()
                tokens.append(self.make_String())
    #For CHAR
            elif self.current_char == '\'':
                self.advance()
                tokens.append(self.make_char())
    
    #For Acessor
            elif(self.current_char == "."):
                self.advance()
                tokens.append(Token(TT_ACESSOR))


    #For Arithematic Operators and Asssignment Operators
            elif(self.current_char == "+"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_ASSIGNMENTOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_PLUS, pos_start = self.pos))
                    # self.advance()
            
            elif(self.current_char == "-"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_ASSIGNMENTOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_MINUS, pos_start = self.pos))
                    # self.advance()
            
            elif(self.current_char == "*"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_ASSIGNMENTOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_MUL, pos_start = self.pos))
                    # self.advance()
            
            elif(self.current_char == "/"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_ASSIGNMENTOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_DIV, pos_start = self.pos))
                    # self.advance()
            
            elif(self.current_char == "%"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_ASSIGNMENTOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_MOD, pos_start = self.pos))
                    # self.advance()

    #Relational Operators 
            elif(self.current_char == "="):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_RELATIONALOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_ASSIGNMENTOP))
                    # self.advance()

            elif(self.current_char == ">"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_RELATIONALOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_RELATIONALOP))
                    # self.advance()
            
            elif(self.current_char == "<"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_RELATIONALOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_RELATIONALOP))
                    # self.advance()
            
            elif(self.current_char == "!"):
                temp = self.current_char
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TT_RELATIONALOP))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_NOT))
                    # self.advance()
            
            elif(self.current_char == ":"):
                temp = self.current_char
                self.advance()
                if(self.current_char == ":"):
                    tokens.append(Token(TT_SCOPERESOLUTION))
                    self.advance()
                else:
                    # self.current_char = temp
                    tokens.append(Token(TT_INHERITANCE_INITIATOR))
                    # self.advance()

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
            elif self.current_char == '[':
                tokens.append(Token(TT_LPARENS))
                self.advance()
            elif self.current_char == ']':
                tokens.append(Token(TT_RPARENS))
                self.advance()
            
            else:
                posi_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], Error.IllegalCharError(posi_start, self.pos ,"'" + char + "'")
        
        tokens.append(Token(TT_ENDMARKER,  pos_start = self.pos))
        return tokens, None

#######################################
# RUN
#######################################

def run(text):
    #for tokens
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    #for parser
    par = Parser.Parser(tokens)
    ast = par.parse()

    return ast, None

            


