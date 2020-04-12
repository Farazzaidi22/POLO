import polo
import Symbol_table as ST
import Class_Table as CT
import Class_Data_Table as CDT

s1   = ST.SymbolTable()
c1   = CT.ClassTable()

Label_stack = []
Label_no    = 0 

def CreateScope():
    global Label_no, Label_stack
    Label_stack.append(Label_no)
    Label_no += 1
    return (Label_no - 1)

def DestroyScope():
    s_no = Label_stack.pop()
    if(Label_stack != None):
        return s_no
    else:
        return -1



def Compatibility(LT, RT, OP):
    
    if(LT == "INT_Number" and RT == "INT_Number"):
        if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'Mod' or OP == 'AssignmentOperator'):
            print("compat match")
            return LT
    
    if(LT == "int" and RT == "INT_Number"):
        if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'Mod' or OP == 'AssignmentOperator'):
            print("compat match")
            return LT
    
    if(LT == "int" and RT == "int"):
        if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'Mod' or OP == 'AssignmentOperator'):
            print("compat match")
            return LT

    if(LT == "float" and RT == "FLOAT_Number"):
        if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'AssignmentOperator'):
            print("compat match")
            return LT
    
    if(LT == "FLOAT_Number" and RT == "FLOAT_Number"):
        if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'AssignmentOperator'):
            print("compat match")
            return LT

    if(LT == "float" and RT == "float"):
        if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'AssignmentOperator'):
            print("compat match")
            return LT
    
    if(LT == "float" and RT == "int"):
        if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'AssignmentOperator'):
            print("compat match")
            return LT
    
    if(LT == "int" and RT == "float"):
        if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'AssignmentOperator'):
            print("compat match")
            return RT

    
    if(LT == "string" and RT == "string"):
        if(OP == 'PLUS'):
            print("compat match")
            return LT
    
    if(OP == "RelationalOperator" or OP == "Logical_Operator"):
        print("T or F")
        return "T or F"
    
    # if(LT == RT):
    #     #  if(OP == 'PLUS' or OP == 'MINUS' or OP == 'MUL' or OP == 'DIV' or OP == 'AssignmentOperator'):
    #     print("compat match of AL")
    #     return LT
    

def Dot_Compatibility(LT, RT, OP):
    if(OP == "Acessor"):
        RT_T = c1.LookUp_CDT(LT, RT)
        if(RT_T):
            LT = RT_T
            print("can call")
            return LT
        else:
            print(LT + " can't call " + RT + " class obj")
            return False


def Func_LookUp(CN, N,AL):
    if(CN == None):# and bool_global == True):
        t2 = s1.lookUp_fun(N,AL)
    elif(CN != None):# and bool_global == False):
        t2 = c1.lookUpFunc_CDT(CN,N, AL)
    
    if(t2 == None):
        print(N, " is not declared in this scope")
        return None
    else:
        print("function found")
        return t2



