#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
ALPHABETS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
SPECIALCHARACTERS ='!@#$%^&|~`+-*/\\='


KeyWord             = ['class', 'static', 'enum', 'return', 'break', 'continue','new','meth']
DataType            = ['int', 'float', 'string', 'char', 'bool', 'var']
loops               = ['for', 'while']
conditional         = ['if', 'else']
Access_Modifiers    = ['public', 'private','protected']
Type_Modifers       = ['virtual','override']
Logical_Operator    = ['and', 'or', 'not']
puntuators          = [';', ',', '\n', ':', '[', ']', '{', '}', '(', ')', '.']


# def SDT(n):
#     for (i,j,k) in zip(KeyWord.item , loops, DataType):
#         if KeyWord[i] == n:
#             return 1
#         elif loops[j] == n:
#             return 2
#         elif DataType[k] == n:
#             return 3
#         else:
#             return False

#######################################
# ERRORS
#######################################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

#######################################
# POSITION
#######################################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self
    
    def back(self, current_char):
        self.idx -= 1
        self.col -= 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#######################################
# TOKENS
#######################################

TT_ERROR = 'Error'

TT_ACESSOR = 'Acessor'
TT_SCOPERESOLUTION = 'ScopeResolution'
TT_INHERITANCE_INITIATOR = 'inheritant initiator'

TT_KW       = 'KeyWord'
TT_ID       = 'Variable'
TT_LOOP     = 'loop'

TT_STRING   = 'STRING'
TT_CHAR     = 'CHAR'

TT_INT		= 'INT_Number'
TT_FLOAT    = 'FLOAT_Number'
TT_VARIABLE = 'Variable'

TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_MOD      = 'Mod'


TT_ASSIGNMENTOP        = 'AssignmentOperator'
TT_RELATIONALOP     = 'RelationalOperator'
TT_NOT              = 'NOT'

TT_LPARENR   = 'LPARENRound'
TT_RPARENR   = 'RPARENRound'
TT_LPARENC   = 'LPARENCurly'
TT_RPARENC   = 'RPARENCurly'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
    
    def back(self):
        self.pos.back(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx != None else None
 

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '\n':
                self.advance()
            elif self.current_char in (DIGITS) or (ALPHABETS):
                tokens.append(self.make_both())
            # elif self.current_char in ALPHABETS:
            #     tokens.append(self.make_variable())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
                # self.back()
                # print(self.current_char)
                # break
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPARENR))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPARENR))
                self.advance()
            elif self.current_char == '\"':
                #temp = self.current_char
                self.advance()
                tokens.append(self.make_string())
            elif self.current_char == '\'':
                #temp = self.current_char
                self.advance()
                tokens.append(self.make_char())
            elif self.current_char == '.':
                self.advance()
                if self.current_char in ALPHABETS:
                    tokens.append(self.make_variable())
                else:
                    tokens.append(Token(TT_ACESSOR))

            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None



    def make_char(self):
        char_str= ''
        quot_count = 0

        while self.current_char != None and self.current_char in ALPHABETS + '\'' + ' \t' + DIGITS:
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



    def make_string(self):
        num_str = ''
        quot_count = 0

        while self.current_char != None and self.current_char in ALPHABETS + '\"' + ' \t' + DIGITS:
            
            if self.current_char == '\"':
                if quot_count == 0: 
                    quot_count += 1
                    self.advance()
                    if quot_count == 1:
                        return Token(TT_STRING, num_str)
            else:
                num_str += self.current_char
            self.advance()
        
        
        
        # if quot_count ==1:
        #     return Token(TT_STRING, num_str)
        # else:
            
        #     print("error, \" is missing")


    def make_both(self):
        num_str = ''
        var_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS +ALPHABETS + '.':
            if self.current_char in ALPHABETS:
                #var_str = num_str
                # if self.current_char == '.':
                #     if dot_count == 1: 
                #         break
                #     dot_count += 1
                #     var_str += '.'
            #else:
                var_str += self.current_char
                #self.advance()

            if self.current_char in DIGITS:
                # if self.current_char == '.':
                #     if dot_count == 1: 
                #         break
                #     dot_count += 1
                #     num_str += '.'
            # else:
                num_str += self.current_char
            
            if self.current_char == '.' and var_str == '':
                    if dot_count == 1:
                        break
                    dot_count += 1
                    num_str += '.'
            elif self.current_char == '.' and var_str != '':
                if dot_count == 1: 
                    break
                dot_count += 1
                var_str += '.'

            self.advance()
        
        if(var_str != '' and num_str != ''):
            var_str= var_str+num_str
            return Token(TT_ID, var_str)
        
        elif(var_str != '' and num_str == ''):
            var_str= var_str+num_str
            return Token(TT_ID, var_str)
        
        elif dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))





    # def make_number(self):
    #     num_str = ''
    #     var_str = ''
    #     dot_count = 0

    #     while self.current_char != None and self.current_char in DIGITS + '.':
    #         if self.current_char == '.':
    #             if dot_count == 1: break
    #             dot_count += 1
    #             num_str += '.'
    #         else:
    #             num_str += self.current_char
    #         self.advance()

    #     if dot_count == 0:
    #         return Token(TT_INT, int(num_str))
    #     else:
    #         return Token(TT_FLOAT, float(num_str))


    # def make_variable(self):
    #     var_str = ''
    #     #dot_count = 0

    #     while self.current_char != None and self.current_char in ALPHABETS + DIGITS + '.':
    #         var_str += self.current_char
    #         self.advance()

    #         if self.current_char == '.':
    #             self.advance()
    #             if self.current_char in DIGITS:
    #                 self.back()
    #                 break
    #             else:
    #                 var_str += '.'
        

    #     if( var_str in DataType):
    #         return Token(TT_KW, (var_str))
    #     elif(var_str in loops):
    #         return Token(TT_LOOP, (var_str))
    #     else:
    #         return Token(TT_ID, (var_str))

        # x = SDT(var_str)
        # if x== 1:
        #     return Token(TT_KW, (var_str))
        # elif x== 2:
        #     return Token(TT_LOOP, (var_str))
        # else:
        #     return Token(TT_ID, (var_str))
    
#######################################
# RUN
#######################################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error