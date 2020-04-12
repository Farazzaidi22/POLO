import polo
import nodes
import Error
import Symbol_table as ST
import Class_Table as CT
import Class_Data_Table as CDT
import Extra_function as EF
import ICG


s1 = ST.SymbolTable()
c1 = CT.ClassTable()

g_scp = EF.CreateScope()
print(g_scp, " global started")

bool_global = True

class Parser:
    def __init__(self, tokens):
        self.tokens  = tokens
        self.tok_idx = -1
        self.advanceForPar()
    
    def advanceForPar(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

        return self.current_tok

    def parse(self):
        res = self.Definition()
        return res
    

    def Definition(self):
        if(self.current_tok.type == polo.TT_DT):
            CN = None
            Am = None
            S= g_scp
            if(self.Dec(CN, Am, S)):
                if(self.Definition()):
                    return True
                else:
                    return False
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_ID):
            CN = None
            Am = None
            S= g_scp
            if(self.newAssign_St(CN, Am, S)):
                if(self.Definition()):
                    return True
                else:
                    return False
            else:
                return False

        elif(self.current_tok.type == polo.TT_ACESSORMOD or self.current_tok.type == polo.TT_CLASS):
            if(self.ClassDec()):
                if(self.Definition()):
                    return True
                else:
                    return False
            else:
                return False

        elif(self.current_tok.type == polo.TT_METH):
            CN = None
            AM = None
            if(self.func_dec(CN, bool_global,AM)):
                if(self.Definition()):
                    return True
                else:
                    return False
            else:
                return False

        elif(self.current_tok.type == polo.TT_ENDMARKER):
            g_scp_end = EF.DestroyScope()
            print(g_scp_end, " global finished")
            # file1.close() 
            return True
        else:
            return False
    


    def listt(self):
        if(self.current_tok.type == polo.TT_TERMINATOR):
            self.advanceForPar()
            return True
        else:
            return None
    
    def array1(self):
        if(self.current_tok.type == polo.TT_LPARENS):
            self.advanceForPar()
            if(self.OE()):
                if(self.current_tok.type == polo.TT_RPARENS):
                    self.advanceForPar()
                    return True
                else:
                    return False
            else:
                return False

        elif(self.current_tok.type == polo.TT_ASSIGNMENTOP or 
        self.current_tok.type == polo.TT_MUL or self.current_tok.type == polo.TT_DIV or 
        self.current_tok.type == polo.TT_MOD or self.current_tok.type == polo.TT_PLUS or 
        self.current_tok.type == polo.TT_MINUS or self.current_tok.type == polo.TT_RELATIONALOP or 
        self.current_tok.type == polo.TT_LOGICALOP or self.current_tok.type == polo.TT_SEPARATOR or 
        self.current_tok.type == polo.TT_TERMINATOR or self.current_tok.type == polo.TT_ACESSOR or 
        self.current_tok.type == polo.TT_RPARENR or self.current_tok.type == polo.TT_LPARENR 
        or self.current_tok.type == polo.TT_RPARENS):
            return True
        
        else:
            return False
    
    def DataType(self):
        if(self.current_tok.type == polo.TT_DT):
            t = self.current_tok.value
            self.advanceForPar()
            return t
        else:
            return None
    
    def OnlyID(self):
        if(self.current_tok.type == polo.TT_ID):
            t = self.current_tok.value
            self.advanceForPar()
            if(self.array1()):
                return t
            else:
                return None
        else:
            return None
    
    def ClassDec(self):
        if(self.current_tok.type == polo.TT_ACESSORMOD or self.current_tok.type == polo.TT_CLASS):
            if(self.AM()):
                if(self.current_tok.type == polo.TT_CLASS):
                    self.advanceForPar()
                    if(self.current_tok.type == polo.TT_ID):
                        n1 = self.current_tok.value
                        self.advanceForPar()
                        P1 = self.inHerit()
                        if(P1):
                            c1.Insert_CT(n1, P1)
                            if(self.current_tok.type == polo.TT_LPARENC):
                                self.advanceForPar()
                                if(self.ClassBody(n1)):
                                    if(self.current_tok.type == polo.TT_RPARENC):
                                        self.advanceForPar()
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

        else:
            return False
    
    def AM(self):
        if(self.current_tok.type == polo.TT_ACESSORMOD):
            AM = self.current_tok.value
            self.advanceForPar()
            return AM
            
        elif(self.current_tok.type == polo.TT_CLASS or self.current_tok.type == polo.TT_DT 
        or self.current_tok.type == polo.TT_ID):
            return True
        
        else:
            return None
    
    def inHerit(self):
        if(self.current_tok.type == polo.TT_INHERITANCE_INITIATOR):
            self.advanceForPar()
            if(self.current_tok.type == polo.TT_ID):
                n2 = self.current_tok.value
                T2 = c1.lookUp_CT(n2)
                self.advanceForPar()
                return T2
            else:
                return None
    
        elif(self.current_tok.type == polo.TT_LPARENC):
            return True
        
        else:
            return False
    
    def ClassBody(self, CN):
        if(self.current_tok.type == polo.TT_METH or self.current_tok.type == polo.TT_ACESSORMOD or 
        self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID):
            Am = self.AM()
            S=0
            if(Am):
                if(self.Dec(CN, Am, S)):
                    if(self.ClassBody(CN)):
                        return True
                    else:
                        return False
                elif(self.newAssign_St(CN, Am, S)):
                    if(self.ClassBody(CN)):
                        return True
                    else:
                        return False

                else:
                    return False
            
            elif(self.func_dec(CN, bool_global = False, AM = "public")):
                if(self.ClassBody(CN)):
                    return True
                else:
                    return False
        
        elif(self.current_tok.type == polo.TT_RPARENC):
            return True
        
        else:
            return False

    
    def func_dec(self, CN, bool_global, AM):
        if(self.current_tok.type ==  polo.TT_METH):
            self.advanceForPar()
            if(self.current_tok.type ==  polo.TT_ID):
                n2 = self.current_tok.value
                if(CN == None and bool_global == True):
                    t1 = s1.lookUp(n2,0)
                elif(CN != None and bool_global == False):
                    t1 = c1.LookUp_CDT(CN,n2)
                
                if(t1 != None):
                    print(n2 + " is already declared")
                    return False

                self.advanceForPar()
                if(self.current_tok.type == polo.TT_LPARENR):
                    Scp_no = EF.CreateScope()
                    print(Scp_no, " just started")
                    self.advanceForPar()
                    PL = []
                    pl_ret = self.Dec_Args(CN, PL, Scp_no)
                    print(pl_ret)
                    if(pl_ret):
                        if(self.current_tok.type == polo.TT_RPARENR):
                            if(CN == None and bool_global == True and t1 == None):
                                s1.Insert_ST(n2, pl_ret, g_scp)
                            elif(CN != None and bool_global == False and t1 == None):
                                c1.Insert_CDT(CN, n2, pl_ret, None)
                            self.advanceForPar()
                            if(self.current_tok.type == polo.TT_LPARENC):
                                self.advanceForPar()
                                CN = None 
                                AM = None
                                if(self.MST(CN, AM, Scp_no)):
                                    # rt = self.ret
                                    if(self.current_tok.type == polo.TT_RPARENC):
                                        scp_no_sol = EF.DestroyScope()
                                        print(scp_no_sol, " is finished")
                                        self.advanceForPar()
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    
    def Dec_Args(self, CN, PL, Scp_no):
        if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID):
              
            if(self.current_tok.type == polo.TT_DT):
                t1 = self.Dec_For_Args(CN, PL,Scp_no)
                if(t1):
                    PL.append(t1)
                    t2 = self.MDec_Args(CN, PL, Scp_no)
                    if(t2):
                        # PL.append(t2)
                        return PL
                    else:
                        return PL
                else:
                    return PL
            
            if(self.current_tok.type == polo.TT_ID):
                t1 = self.Assign_St_For_Args(CN, PL, Scp_no)
                if(t1):
                    PL.append(t1)
                    t2 = self.MDec_Args(CN, PL, PL)
                    if(t2):
                        # PL.append(t2)
                        return PL
                    else:
                        return PL
                else:
                    return PL
            
        elif(self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENR):
            return True
        
        else:
            return False
    
    def MDec_Args(self, CN, PL, Scp_no):
        if(self.current_tok.type == polo.TT_SEPARATOR):
            self.advanceForPar()
            if(self.Dec_Args(CN, PL, Scp_no)):
                if(self.MDec_Args(CN, PL, Scp_no)):
                    return True
                else:
                    return False
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_RPARENR):
            return True

        else:
            return False

    def Dec_For_Args(self, CN, PL, Scp_no):
        if(self.current_tok.type == polo.TT_DT):
            t1 = self.DataType()
            if(t1):
                n1 = self.OnlyID()
                if(n1):
                    if(CN == None):
                        s1.Insert_ST(n1,t1,Scp_no)
                    elif(CN != None):
                        c1.Insert_CDT(CN,n1, t1, "private")
                    else:
                        print("masla ha") 

                if(self.new_INIT1(t1)):
                    return t1
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def Assign_St_For_Args(self, CN, PL, Scp_no):
        if(self.current_tok.type == polo.TT_ID):
            n1 = self.current_tok.value
            t1 = c1.lookUp_CT(n1)
            self.advanceForPar()
            if(t1):
                n2 = self.OnlyID()
                if(n2):
                    if(CN == None):
                        s1.Insert_ST(n2,t1,Scp_no)
                    elif(CN != None):
                        c1.Insert_CDT(CN,n2, t1, "private")
                if(self.new_INIT1(t1)):
                    return t1
                else:
                    return False
            else:
                return False
        else:
            return False

    def new_INIT1(self, t1):
        if(self.current_tok.type == polo.TT_ASSIGNMENTOP): 
            if(self.current_tok.type == polo.TT_ASSIGNMENTOP):
                OP = self.current_tok.value
                self.advanceForPar()
                if(self.INIT2(t1, OP)):
                    if(self.new_INIT1(t1)):
                        return True
                    else:
                        return False
                else:
                    return False
        elif(self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENR):
            return True
        else:
            return False
    
    def func_call(self, CN, AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID):
            if(self.fac_ID(CN, AM, Scp_no)):
                if(self.listt()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def Call_Args(self,CN, AM, Scp_no, AL):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type in polo.TT_INT or 
        self.current_tok.type == polo.TT_LPARENR or self.current_tok.type == polo.TT_FLOAT or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):

            if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or 
            self.current_tok.type == polo.TT_LPARENR or self.current_tok.type == polo.TT_NOT or 
            self.current_tok.type == polo.TT_BOOL):
                
                t1 = self.OE(None,CN ,AM, Scp_no)
                AL.append(t1) 
                if(t1):
                    if(self.MCall_Args(CN, AM, Scp_no, AL)):
                        return AL
                    else:
                        return False
                else:
                    return False
            else:
                return False
            
        elif(self.current_tok.type == polo.TT_RPARENR):
            return True
        
        else:
            return False


    def MCall_Args(self,CN, AM, Scp_no, AL):
        if(self.current_tok.type == polo.TT_SEPARATOR):
            if(self.current_tok.type == polo.TT_SEPARATOR):
                self.advanceForPar()
                if(self.Call_Args(CN, AM, Scp_no,AL)):
                    return AL
                else:
                    return False
            else:
                return False

        elif(self.current_tok.type == polo.TT_RPARENR):
            return AL
        
        else:
            return False
    

    def Dec(self, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_DT):
            t1 = self.DataType()
            if(t1):
                n1 = self.OnlyID()
                if(n1):
                    if((AM == True or AM == None) and CN == None):
                        s1.Insert_ST(n1,t1,Scp_no)
                    elif(AM == True and CN != None):
                        c1.Insert_CDT(CN,n1, t1, "private")
                    else:
                        c1.Insert_CDT(CN,n1, t1, AM) 
    
                    if(self.INIT1(t1, CN, AM, Scp_no)):
                        if(self.listt()):
                            return t1
                        else:    
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def INIT1(self, t1, CN, AM, Scp_no):
        if(self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_ASSIGNMENTOP):
            
            if(self.current_tok.type == polo.TT_SEPARATOR):
                self.advanceForPar()
                n2 = self.OnlyID()
                if(n2):
                    if((AM == True or AM == None) and CN == None):
                        s1.Insert_ST(n2,t1,Scp_no)
                    elif(AM == True and CN != None):
                        c1.Insert_CDT(CN,n2, t1, "private")
                    else:
                        c1.Insert_CDT(CN,n2, t1, AM)
                    if(self.INIT1(t1, CN, AM, Scp_no)):
                        return True
                    else:
                        return False
                else:
                    return False
            
            elif(self.current_tok.type == polo.TT_ASSIGNMENTOP):
                OP = self.current_tok.type
                self.advanceForPar()
                if(self.INIT2(t1, OP,CN, AM, Scp_no)):
                    if(self.INIT1(t1, CN, AM, Scp_no)):
                        return True
                    else:
                        return False
                else:
                    return False
            
        elif(self.current_tok.type == polo.TT_TERMINATOR or self.current_tok.type == polo.TT_RPARENR
        or self.current_tok.type == polo.TT_RPARENC):
            return True
        
        else:
            return False
    

    def INIT2(self, t1, OP,CN, AM, Scp_no):
        if(self.current_tok.type in polo.TT_INT or self.current_tok.type == polo.TT_LPARENC or self.current_tok.type == polo.TT_ID or
        self.current_tok.type == polo.TT_LPARENR or self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL or 
        self.current_tok.type == polo.TT_NEW or self.current_tok.type in polo.TT_FLOAT):
            
            if(self.current_tok.type == polo.TT_LPARENC):
                self.advanceForPar()
                if(self.current_tok.type in polo.TT_INT):
                    self.advanceForPar()
                    if(self.more_Const()):
                        if(self.current_tok.type == polo.TT_RPARENC):
                            self.advanceForPar()
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            
            elif(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or
            self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
                t2 = self.OE(t1,CN, AM, Scp_no)
                chk = EF.Compatibility(t1,t2,OP)
                if(chk):
                    return chk
                else:
                    print("type mismatch error")
          
            elif(self.current_tok.type == polo.TT_NEW):
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_ID ):
                    self.advanceForPar()
                    if(self.current_tok.type == polo.TT_LPARENR):
                        self.advanceForPar()
                        if(self.Call_Args(self,CN, AM, Scp_no, None)):
                            self.advanceForPar()
                            if(self.current_tok.type == polo.TT_RPARENR):
                                self.advanceForPar()
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def more_Const(self):
        if(self.current_tok.type == polo.TT_SEPARATOR):
            self.advanceForPar()
            if(self.current_tok.type in polo.TT_INT):
                self.advanceForPar()
                if(self.more_Const()):
                    return True
                else:
                    return False
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_RPARENC):
            return True
        
        else:
            return False


    def newAssign_St(self, CN,AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID):
            t1 = self.Assign_St(CN,None ,AM,Scp_no)
            if(t1):
                if(self.listt()):
                    return t1
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def Assign_St(self, CN,PL,  AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID):
            t1 = self.fac_ID(CN, AM, Scp_no)
            if(t1):
                return t1
            else:
                return False
        else:
            return False
    

    def OE(self,t1,CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or 
        self.current_tok.type == polo.TT_FLOAT or self.current_tok.type == polo.TT_CHAR or 
        self.current_tok.type == polo.TT_STRING or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            
            t2 = self.AE(t1, CN ,AM, Scp_no)
            if(t2):
                t2 = self.OEe(t2, CN ,AM, Scp_no)
                if(t2):
                    return t2
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def OEe(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_LOGICALOP):  
            if(self.current_tok.value == "or"):
                OP = self.current_tok.type
                self.advanceForPar()
                t2 = self.AE(t1, CN ,AM, Scp_no)
                if(t2):
                    t1 = EF.Compatibility(t1, t2, OP)
                    if(t1):
                        t1 = self.OEe(t1, CN ,AM, Scp_no)
                        if(t1):
                            return t1
                        else:
                            return None
                    else:
                        return False
                else:
                    return False
        
        elif(self.current_tok.type == polo.TT_ASSIGNMENTOP or 
        self.current_tok.type == polo.TT_RPARENS or self.current_tok.type == polo.TT_RPARENR or
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_TERMINATOR):
            return t1
        
        else:
            return False

    
    def AE(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or 
        self.current_tok.type == polo.TT_FLOAT or self.current_tok.type == polo.TT_CHAR or 
        self.current_tok.type == polo.TT_STRING or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            
            t1 = self.RE(t1, CN ,AM, Scp_no)
            if(t1):
                t1 = self.AEe(t1, CN ,AM, Scp_no)
                if(t1):
                    return t1
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def AEe(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_LOGICALOP):
            if(self.current_tok.value == "and"):
                OP = self.current_tok.type
                self.advanceForPar()
                t2 = self.RE(t1, CN ,AM, Scp_no)
                if(t2):
                    t1 = EF.Compatibility(t1, t2, OP)
                    if(t1):
                        t1 = self.AEe(t1, CN ,AM, Scp_no)
                        if(t1):
                            return t1
                        else:
                            return None
                    else:
                        return False
                else:
                    return False
            else:
                return t1
        
        elif(self.current_tok.type == polo.TT_ASSIGNMENTOP or 
        self.current_tok.type == polo.TT_RPARENS or self.current_tok.type == polo.TT_RPARENR or
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_TERMINATOR):
            return t1
        
        else:
            return False
    

    def RE(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or 
        self.current_tok.type == polo.TT_FLOAT or self.current_tok.type == polo.TT_CHAR or 
        self.current_tok.type == polo.TT_STRING or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            
            t1 = self.E(t1, CN ,AM, Scp_no)
            if(t1):
                t1 = self.REe(t1, CN ,AM, Scp_no)
                if(t1):
                    return t1
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def REe(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_RELATIONALOP):
            OP = self.current_tok.type
            self.advanceForPar()
            t2 = self.E(t1, CN ,AM, Scp_no)
            if(t2):
                t1 = EF.Compatibility(t1, t2, OP)
                if(t1):
                    t1 = self.REe(t1, CN ,AM, Scp_no)
                    if(t1):
                        return t1
                    else:
                        return None
                else:
                    return False
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_LOGICALOP  or 
        self.current_tok.type == polo.TT_ASSIGNMENTOP or self.current_tok.type == polo.TT_RPARENS or
        self.current_tok.type == polo.TT_RPARENR or 
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_TERMINATOR):
            return t1
        else:
            return False
    

    def E(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or 
        self.current_tok.type == polo.TT_FLOAT or self.current_tok.type == polo.TT_CHAR or 
        self.current_tok.type == polo.TT_STRING or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            t1 = self.T(t1, CN ,AM, Scp_no)
            if(t1):
                t1 = self.Ee(t1, CN ,AM, Scp_no)
                if(t1):
                    return t1
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def Ee(self,t1,CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_PLUS or self.current_tok.type == polo.TT_MINUS):
            OP = self.current_tok.type
            self.advanceForPar()
            t2 = self.T(t1, CN ,AM, Scp_no)
            if(t2):
                t1 = EF.Compatibility(t1, t2, OP)
                if(t1):
                    t1 = self.Ee(t1, CN ,AM, Scp_no)
                    if(t1):
                        return t1
                    else:
                        return None
                else:
                    return False
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_RELATIONALOP or 
        self.current_tok.type == polo.TT_LOGICALOP  or self.current_tok.type == polo.TT_ASSIGNMENTOP 
        or self.current_tok.type == polo.TT_RPARENS or self.current_tok.type == polo.TT_SEPARATOR or
        self.current_tok.type == polo.TT_RPARENR or self.current_tok.type == polo.TT_TERMINATOR):
            return t1
        
        else:
            return False


    def T(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or 
        self.current_tok.type == polo.TT_FLOAT or self.current_tok.type == polo.TT_CHAR or 
        self.current_tok.type == polo.TT_STRING or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            
            t1 = self.F(t1,CN ,AM, Scp_no)
            if(t1):
                t1 = self.Te(t1, CN ,AM, Scp_no)
                if(t1):
                    return t1
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def Te(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_MUL or 
        self.current_tok.type == polo.TT_DIV or self.current_tok.type == polo.TT_MOD):
            OP = self.current_tok.type
            self.advanceForPar()
            t2 = self.F(t1, CN ,AM, Scp_no)
            if(t2):
                # ICG.manage_st(t1, t2, OP)
                t1 = EF.Compatibility(t1, t2, OP)
                if(t1):
                    t1 = self.Te(t1, CN ,AM, Scp_no)
                    if(t1):
                        return t1
                    else:
                        return None
                else:
                    return False
            else:
                return False
           
        elif(self.current_tok.type == polo.TT_PLUS or self.current_tok.type == polo.TT_MINUS or
        self.current_tok.type == polo.TT_RELATIONALOP or self.current_tok.type == polo.TT_LOGICALOP  or 
        self.current_tok.type == polo.TT_ASSIGNMENTOP or self.current_tok.type == polo.TT_RPARENS or 
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENR or
        self.current_tok.type == polo.TT_TERMINATOR):
            return t1
        
        else:
            return False

    def F(self,t1, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            
            if(self.current_tok.type == polo.TT_ID):
                t1 = self.fac_ID(CN ,AM, Scp_no)
                if(t1):
                    return t1
            
            elif(self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_FLOAT or 
            self.current_tok.type == polo.TT_CHAR or self.current_tok.type == polo.TT_STRING):
                t1 = self.current_tok.type
                self.advanceForPar()
                return t1 
            
            elif(self.current_tok.type == polo.TT_LPARENR):
                self.advanceForPar()
                t1 = self.OE(t1, CN ,AM, Scp_no)
                if(t1):
                    if(self.current_tok.type == polo.TT_RPARENR):
                        self.advanceForPar()
                        return t1
                    else:
                        return False
                else:
                    return False

            elif(self.current_tok.type == polo.TT_NOT):
                t2 = self.current_tok.value
                self.advanceForPar()
                if(self.F(t2, CN ,AM, Scp_no)):
                    return t2
                else:
                    return False
            
            elif(self.current_tok.type == polo.TT_BOOL):
                t1 = self.current_tok.value
                self.advanceForPar()
                return t1
            else:
                return False
    
    def return_st(self, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_RET):
            self.advanceForPar()
            t1 = self.OE(None,CN ,AM, Scp_no)
            if(t1):
                if(self.listt()):
                    return t1
                else:
                    return False
            else:
                return False
        
        elif(self.current_tok.type == polo.polo.TT_RPARENC):
            return True

        else:
            return False
    
    def break_st(self):
        if(self.current_tok.type == polo.TT_BREAK):
            self.advanceForPar()
            if(self.listt()):
                return True
            else:
                return False
        else:
            return False
    
    def If_st(self, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_IF):
            ICG.StartLabel()
            self.advanceForPar()
            if(self.current_tok.type == polo.TT_LPARENR):
                Scp_no2 = EF.CreateScope()
                print(Scp_no2 , " just started")
                self.advanceForPar()
                t1 = self.OE(None, CN ,AM, Scp_no)
                ICG.manage_Cod()
                if(t1):
                    if(self.current_tok.type == polo.TT_RPARENR):
                        self.advanceForPar()
                        if(self.current_tok.type == polo.TT_LPARENC):
                            self.advanceForPar()
                            if(self.MST(CN ,AM, Scp_no)):
                                if(self.current_tok.type == polo.TT_RPARENC):
                                    Scp_no2_fin = EF.DestroyScope()
                                    print(Scp_no2_fin , " is finished")
                                    ICG.FinishLabel()
                                    self.advanceForPar()
                                    if(self.Else_st(CN ,AM, Scp_no)):
                                        return True
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def Else_st(self, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_ELSE):
            self.advanceForPar()
            if(self.current_tok.type == polo.TT_LPARENC):
                Scp_no3 = EF.CreateScope()
                print(Scp_no3 , " just started")
                self.advanceForPar()
                if(self.MST(CN ,AM, Scp_no3)):
                    if(self.current_tok.type == polo.TT_RPARENC):
                        Scp_no3_fin = EF.DestroyScope()
                        print(Scp_no3_fin , " is finished")
                        self.advanceForPar()
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or 
        self.current_tok.type == polo.TT_WHILE or self.current_tok.type == polo.TT_FOR or 
        self.current_tok.type == polo.TT_IF or self.current_tok.type == polo.TT_RET or 
        self.current_tok.type == polo.TT_RPARENC or self.current_tok.type == polo.TT_BREAK):
            return True
        
        else:
            return False
    
    def For_st(self, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_FOR):
            ICG.StartLabel()
            self.advanceForPar()
            if(self.current_tok.type == polo.TT_ID):
                n1 = self.current_tok.value
                if(CN == None):
                    t2 = s1.lookUp(n1,Scp_no)
                elif(CN != None):
                    t2 = c1.LookUp_CDT(CN, n1)
                if(t2 == None):
                    print(n1 + " is not declared in this scope")
                    return None
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_IN):
                    self.advanceForPar()
                    if(self.current_tok.type == polo.TT_RANGE):
                        self.advanceForPar()
                        if(self.current_tok.type == polo.TT_LPARENR):
                            Scp_no2 = EF.CreateScope()
                            print(Scp_no2 , " just started")
                            self.advanceForPar()
                            t3 = self.OE(None ,CN ,AM, Scp_no)
                            ICG.manage_Cod()
                            if(t3):
                                if(self.mCond(CN ,AM, Scp_no)):
                                    if(self.current_tok.type == polo.TT_RPARENR):
                                        self.advanceForPar()
                                        if(self.current_tok.type == polo.TT_LPARENC):
                                            self.advanceForPar()
                                            if(self.MST(CN ,AM, Scp_no)):
                                                if(self.current_tok.type == polo.TT_RPARENC):
                                                    Scp_no2_fin = EF.DestroyScope()
                                                    print(Scp_no2_fin , " is finished")
                                                    ICG.FinishLabel()
                                                    self.advanceForPar()
                                                    return True
                                                else:
                                                    return False
                                            else:
                                                return False
                                        else:
                                            return False
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def mCond(self, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_SEPARATOR):
            self.advanceForPar()
            if(self.OE(None , CN ,AM, Scp_no)):
                return True
            else:
                return False
        elif(self.current_tok.type == polo.TT_RPARENR):
            return True
        else:
            return False
    
    def While_st(self, CN ,AM, Scp_no):
        if(self.current_tok.type == polo.TT_WHILE):
            ICG.StartLabel()
            self.advanceForPar()
            if(self.current_tok.type == polo.TT_LPARENR):
                Scp_no2 = EF.CreateScope()
                print(Scp_no2 , " just started")
                self.advanceForPar()
                t1 = self.OE(None, CN ,AM, Scp_no)
                ICG.manage_Cod()
                if(t1):
                    if(self.current_tok.type == polo.TT_RPARENR):
                        self.advanceForPar()
                        if(self.current_tok.type == polo.TT_LPARENC):
                            self.advanceForPar()
                            if(self.MST(CN ,AM, Scp_no)):
                                if(self.current_tok.type == polo.TT_RPARENC):
                                    Scp_no2_fin = EF.DestroyScope()
                                    print(Scp_no2_fin , " is finished")
                                    ICG.FinishLabel()
                                    self.advanceForPar()
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def SST(self, CN, AM, Scp_no):
        if(self.current_tok.type == polo.TT_DT):
            if(self.Dec(CN, AM, Scp_no)):
                return True
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_ID):
            if(self.func_call(CN, AM, Scp_no)):
                return True
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_ID):
            if(self.newAssign_St(CN, AM, Scp_no)):
                return True
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_WHILE):
            if(self.While_st(CN, AM, Scp_no)):
                return True
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_FOR):
            if(self.For_st(CN, AM, Scp_no)):
                return True
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_IF):
            if(self.If_st(CN, AM, Scp_no)):
                return True
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_RET):
            if(self.return_st(CN, AM, Scp_no)):
                return True
            else:
                return False
        
        elif(self.current_tok.type == polo.TT_BREAK):
            if(self.break_st(CN, AM, Scp_no)):
                return True
            else:
                return False
        
        else:
            return False

    
    def MST(self, CN, AM, Scp_no):
        if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_WHILE or
        self.current_tok.type == polo.TT_FOR or self.current_tok.type == polo.TT_IF or self.current_tok.type == polo.TT_RET or
        self.current_tok.type == polo.TT_BREAK ):
            
            if(self.SST(CN, AM, Scp_no)):
                if(self.MST(CN, AM, Scp_no)):
                    return True
                else:
                    return False
            else:
                return False
        
        elif (self.current_tok.type == polo.TT_RPARENC):
            return True
        
        else:
            return False


    def fac_ID(self, CN, AM, Scp_no):
            if(self.current_tok.type == polo.TT_ID):
                temp = self.current_tok.type
                n1 = self.current_tok.value
                self.advanceForPar()
                
                #obj dec
                if(self.current_tok.type == polo.TT_ID):
                    t1 = c1.lookUp_CT(n1)
                    if(t1):
                        if(self.ID_options(t1, CN, AM, Scp_no)):
                            return t1
                        else:
                            return False
                
                #func call
                elif(self.current_tok.type == polo.TT_LPARENR):
                    if(self.ID_options(n1, CN, AM, Scp_no)):
                        return n1
                    else:
                        return False

                
                #rest of the stuff
                else:
                    if(CN == None):
                        t2 = s1.lookUp(n1,Scp_no)
                    elif(CN != None):
                        t2 = c1.LookUp_CDT(CN, n1)
                    else:
                        print("koi masla ha")
                    if(t2):
                        if(self.ID_options(t2, CN, AM,Scp_no)):
                            return t2
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        
    def ID_options(self, t1, CN, AM, Scp_no):
        if(self.current_tok.type == polo.TT_ACESSOR or self.current_tok.type == polo.TT_ASSIGNMENTOP or
        self.current_tok.type == polo.TT_LPARENS or self.current_tok.type == polo.TT_ID 
        or self.current_tok.type == polo.TT_LPARENR):
            
            if(self.current_tok.type == polo.TT_ACESSOR or self.current_tok.type == polo.TT_LPARENR):
                if(self.opt_1(t1, CN, AM, Scp_no)):
                    if(self.ID_options(t1, CN, AM, Scp_no)):
                        return True
                    else:
                        return False

            elif(self.current_tok.type == polo.TT_ASSIGNMENTOP):
                OP = self.current_tok.type
                self.advanceForPar()
                t1 = self.opt_2(t1, CN, AM, Scp_no, OP)
                if(t1):
                    t1 = self.ID_options(t1, CN, AM, Scp_no)
                    if(t1):
                        return t1
                    else:
                        return False
                else:
                    return False

            elif(self.array1()):
                if(self.ID_options(t1, CN, AM, Scp_no)):
                    return True
                else:
                    return False

            elif(self.current_tok.type == polo.TT_ID):
                n1 = self.current_tok.value
                self.advanceForPar()
                if(CN == None):
                    s1.Insert_ST(n1, t1, Scp_no)
                elif(CN != None):
                    c1.Insert_CDT(CN,n1,t1,AM)
                else:
                    print("there is some issue")

                if(self.moreID(t1, CN, AM, Scp_no)):
                    if(self.ID_options(t1, CN, AM, Scp_no)):
                        return True
                    else:
                        return False
                else:
                    return False

        elif(self.current_tok.type == polo.TT_TERMINATOR or self.current_tok.type == polo.TT_SEPARATOR or
        self.current_tok.type == polo.TT_RPARENR or self.current_tok.type == polo.TT_RPARENS or 
        self.current_tok.type == polo.TT_MUL or self.current_tok.type == polo.TT_DIV or 
        self.current_tok.type == polo.TT_MOD
        or self.current_tok.type == polo.TT_PLUS or self.current_tok.type == polo.TT_MINUS or
        self.current_tok.type == polo.TT_RELATIONALOP or self.current_tok.type == polo.TT_LOGICALOP  or 
        self.current_tok.type == polo.TT_ASSIGNMENTOP):
           return True
        
        else:
            return False
    
    def opt_1(self,t1, CN, AM, Scp_no):
        if(self.current_tok.type == polo.TT_ACESSOR or self.current_tok.type == polo.TT_LPARENR):
            
            #dot
            if(self.current_tok.type == polo.TT_ACESSOR):
                OP = self.current_tok.type
                self.advanceForPar()
                n2 = self.OnlyID()
                if(self.current_tok.type == polo.TT_LPARENR):
                    self.advanceForPar()
                    AL = []
                    AL = self.Call_Args(CN, AM, Scp_no, AL)
                    print(AL)
                    if(AL):
                        if(self.current_tok.type == polo.TT_RPARENR):
                            chk = EF.Func_LookUp(t1,n2, AL)
                            self.advanceForPar()
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    chk = EF.Dot_Compatibility(t1, n2, OP)
                
                if(chk):
                    # t2 = self.opt_1(t1, CN, AM, Scp_no)
                    t1 = chk
                    if(self.opt_1(t1, CN, AM, Scp_no)):
                        return t1
                    else:
                        return False
                else:
                    return False
            
            #func call
            elif(self.current_tok.type == polo.TT_LPARENR):
                self.advanceForPar()
                AL = []
                AL = self.Call_Args(CN, AM, Scp_no, AL)
                print(AL)
                if(AL):
                    if(self.current_tok.type == polo.TT_RPARENR):
                        EF.Func_LookUp(CN, t1,AL)
                        self.advanceForPar()
                        return True
                    else:
                        return False
                else:
                    return False
        
        elif(self.current_tok.type == polo.TT_TERMINATOR or self.current_tok.type == polo.TT_SEPARATOR or
        self.current_tok.type == polo.TT_RPARENR or self.current_tok.type == polo.TT_RPARENS or 
        self.current_tok.type == polo.TT_MUL or self.current_tok.type == polo.TT_DIV or self.current_tok.type == polo.TT_MOD
        or self.current_tok.type == polo.TT_PLUS or self.current_tok.type == polo.TT_MINUS or
        self.current_tok.type == polo.TT_RELATIONALOP or self.current_tok.type == polo.TT_LOGICALOP  or 
        self.current_tok.type == polo.TT_ASSIGNMENTOP):
            return t1
        
        else:
            return False
    
    def opt_2(self, t1, CN, AM, Scp_no, OP):
        if(self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_ID or 
        self.current_tok.type == polo.TT_LPARENC or self.current_tok.type == polo.TT_LPARENR or 
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL or 
        self.current_tok.type == polo.TT_NEW):
            
            if(self.current_tok.type == polo.TT_LPARENC):
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_INT):
                    self.advanceForPar()
                    if(self.more_Const()):
                        if(self.current_tok.type == polo.TT_RPARENC):
                            self.advanceForPar()
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

            # elif(self.current_tok.type == polo.TT_ID):
            #     n2 = self.current_tok.value
            #     if(CN == None):
            #         t2 = s1.lookUp(n2,Scp_no)
            #     elif(CN != None):
            #         t2 = c1.LookUp_CDT(CN ,n2)
            #     else:
            #         print("there is a problem")
            #     if(t2):
            #         chk = EF.Compatibility(t1,t2,OP)
            #         if(chk):
            #             self.advanceForPar()
            #             return chk
            #         else:
            #             print("type miss match error")

            #         if(self.opt_1()):
            #             return True
            #         else:
            #             return False
                      
            #     else:
            #         return False

            elif(self.current_tok.type == polo.TT_NEW):
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_ID):
                    self.advanceForPar()
                    if(self.current_tok.type == polo.TT_LPARENR):
                        self.advanceForPar()
                        if(self.Call_Args()):
                            if(self.current_tok.type == polo.TT_RPARENR):
                                self.advanceForPar()
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            
            elif(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or 
            self.current_tok.type == polo.TT_FLOAT or self.current_tok.type == polo.TT_CHAR or 
            self.current_tok.type == polo.TT_STRING or self.current_tok.type == polo.TT_LPARENR or
            self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
                

                t2 = self.OE(t1,CN, AM, Scp_no)
                chk = EF.Compatibility(t1,t2,OP)
                if(chk):
                    return chk
                else:
                    print("type mismatch error")
            
            else:
                return False
    
    def moreID(self, t1, CN, AM, Scp_no):
        if(self.current_tok.type == polo.TT_SEPARATOR):
            self.advanceForPar()

            if(self.current_tok.type == polo.TT_ID):
                n1 = self.current_tok.value
                self.advanceForPar()
                if(CN == None):
                    s1.Insert_ST(n1, t1, Scp_no)
                elif(CN != None):
                    c1.Insert_CDT(CN,n1,t1,AM)
                if(self.moreID(t1,CN, AM, Scp_no)):
                    return True
                else:
                    return False
            else:
                return False
                
        elif(self.current_tok.type == polo.TT_ACESSOR or self.current_tok.type == polo.TT_ASSIGNMENTOP or
        self.current_tok.type == polo.TT_LPARENS or self.current_tok.type == polo.TT_TERMINATOR or 
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENR or 
        self.current_tok.type == polo.TT_RPARENS or self.current_tok.type == polo.TT_MUL or 
        self.current_tok.type == polo.TT_DIV or self.current_tok.type == polo.TT_MOD or 
        self.current_tok.type == polo.TT_PLUS or self.current_tok.type == polo.TT_MINUS or
        self.current_tok.type == polo.TT_RELATIONALOP or self.current_tok.type == polo.TT_LOGICALOP):
            return True
        
        else:
            return False
