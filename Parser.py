import polo
import nodes
import Error

#######################################
# Parse Result
#######################################

# class ParseResult:
#     def __init__(self):
#         self.error = None
#         self.node = None
    
#     def register(self, res):
#         if isinstance(res, ParseResult):
#             if res.error:
#                 self.error = res.error
#                 return res.node
#             return res

#     def success(self, node):
#         self.node = node
#         return self

#     def failure(self, error):
#         self.error = error
#         return error

#######################################
# Parser
#######################################

class Parser:
    def __init__(self, tokens):
        self.tokens  = tokens
        self.tok_idx = -1
        self.advanceForPar()
    
    def advanceForPar(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

            # if self.current_tok == '\n':

        return self.current_tok

    def parse(self):
        res = self.Definition()
        # if self.current_tok.type != polo.TT_ENDMARKER:
        #     return False

        return res
    
    # def Start(self):
    #     if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or 
    #     self.current_tok.type == polo.TT_ACESSORMOD or self.current_tok.type == polo.TT_CLASS or
    #     self.current_tok.type == polo.TT_METH):
    #         if(self.Definition()):
    #             if(self.current_tok.type == polo.TT_METH):
    #                 self.advanceForPar()
    #                 if(self.current_tok.type == polo.TT_MAIN):
    #                     self.advanceForPar()
    #                     if(self.current_tok.type == polo.TT_LPARENR):
    #                         self.advanceForPar()
    #                         if(self.current_tok.type == polo.TT_RPARENR):
    #                             self.advanceForPar()
    #                             if(self.current_tok.type == polo.TT_LPARENC):
    #                                 self.advanceForPar()
    #                                 if(self.MST()):
    #                                     if(self.current_tok.type == polo.TT_RPARENC):
    #                                         self.advanceForPar()
    #                                         return True
    #                                     else:
    #                                         return False
    #                                 else:
    #                                     return False
    #                             else:
    #                                 return False
    #                         else:
    #                             return False
    #                     else:
    #                         return False
    #                 else:
    #                     return False
    #             else:
    #                 return False
    #         else:
    #             return False
    #     else:
    #         return False
    

    def Definition(self):
        if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or 
        self.current_tok.type == polo.TT_ACESSORMOD or self.current_tok.type == polo.TT_CLASS or
        self.current_tok.type == polo.TT_METH or self.current_tok.type == polo.TT_ENDMARKER):
            
            if(self.Dec() or self.func_dec() or self.ClassDec()):
                if(self.Definition()):
                    return True
                else:
                    return False
            elif(self.current_tok.type == polo.TT_ENDMARKER):
                return True
            else:
                return False
        else:
            return False

    def listt(self):
        if(self.current_tok.type == polo.TT_TERMINATOR):
            self.advanceForPar()
            return True
        else:
            return False
    
    def array1(self):
        if(self.current_tok.type == polo.TT_LPARENS or self.current_tok.type == polo.TT_ASSIGNMENTOP or 
        self.current_tok.type == polo.TT_MUL or self.current_tok.type == polo.TT_DIV or 
        self.current_tok.type == polo.TT_MOD or self.current_tok.type == polo.TT_PLUS or 
        self.current_tok.type == polo.TT_MINUS or self.current_tok.type == polo.TT_RELATIONALOP or 
        self.current_tok.type == polo.TT_LOGICALOP or self.current_tok.type == polo.TT_SEPARATOR or 
        self.current_tok.type == polo.TT_TERMINATOR or self.current_tok.type == polo.TT_ACESSOR or 
        self.current_tok.type == polo.TT_RPARENR or self.current_tok.type == polo.TT_LPARENR 
        or self.current_tok.type == polo.TT_RPARENS):
        
            if(self.current_tok.type == polo.TT_LPARENS):
                self.advanceForPar()
                if(self.OE()):
                    if(self.current_tok.type == polo.TT_RPARENS):
                        self.advanceForPar()
                        return True
                    else:
                        return False
            # else:
            #     return False
            return True
        else:
            return False
    
    #self.ID is missing
    def Identity(self):
        if(self.current_tok.type == polo.TT_ID):
            if(self.current_tok.type == polo.TT_ID):
                self.advanceForPar()
                if(self.array1()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def DTorID(self):
        if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID):
            self.advanceForPar()
            return True
        else:
            return False
    
    def OnlyID(self):
        if(self.current_tok.type == polo.TT_ID):
            if(self.current_tok.type == polo.TT_ID):
                self.advanceForPar()
                if(self.array1()):
                    return True
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    
    def ClassDec(self):
        if(self.current_tok.type == polo.TT_ACESSORMOD or self.current_tok.type == polo.TT_CLASS):
            if(self.AM()):
                if(self.current_tok.type == polo.TT_CLASS):
                    self.advanceForPar()
                    if(self.current_tok.type == polo.TT_ID):
                        self.advanceForPar()
                        if(self.inHerit()):
                            if(self.current_tok.type == polo.TT_LPARENC):
                                self.advanceForPar()
                                if(self.ClassBody()):
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
        if(self.current_tok.type == polo.TT_ACESSORMOD or self.current_tok.type == polo.TT_CLASS 
        or self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID):
            if(self.current_tok.type == polo.TT_ACESSORMOD):
                self.advanceForPar()
                return True
            # else:
            #     return False
            return True
        else:
            return False
    
    def inHerit(self):
        if(self.current_tok.type == polo.TT_INHERITANCE_INITIATOR or self.current_tok.type == polo.TT_LPARENC):
            if(self.current_tok.type == polo.TT_INHERITANCE_INITIATOR):
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_ID):
                    self.advanceForPar()
                    return True
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    
    def ClassBody(self):
        if(self.current_tok.type == polo.TT_METH or self.current_tok.type == polo.TT_ACESSORMOD or 
        self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_RPARENC):
            if(self.func_dec()):
                if(self.ClassBody()):
                    return True
                else:
                    return False
            elif(self.AM()):
                if(self.Dec()):
                    if(self.ClassBody()):
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False

    
    def func_dec(self):
        if(self.current_tok.type ==  polo.TT_METH):
            self.advanceForPar()
            if(self.current_tok.type ==  polo.TT_ID):
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_LPARENR):
                    self.advanceForPar()
                    if(self.Dec_Args()):
                        if(self.MDec_Args()):
                            if(self.current_tok.type == polo.TT_RPARENR):
                                self.advanceForPar()
                                if(self.current_tok.type == polo.TT_LPARENC):
                                    self.advanceForPar()
                                    if(self.MST()):
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
    
    def Dec_Args(self):
        if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or 
        self.current_tok.type == polo.TT_SEPARATOR or  self.current_tok.type == polo.TT_RPARENR):
            if(self.DTorID()):
                if(self.OnlyID()):
                    return True
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    
    def MDec_Args(self):
        if(self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENR):
            if(self.current_tok.type == polo.TT_SEPARATOR):
                self.advanceForPar()
                if(self.Dec_Args()):
                    if(self.MDec_Args()):
                        return True
                    else:
                        return False
                else:
                    return False
                # if(self.DTorID()):
                #     if(self.OnlyID()):
                #         return True
                #     else:
                #         return False
                # else:
                #     return False
            # else:
            #     return False
            return True
        else:
            return False
    
    def func_call(self):
        if(self.current_tok.type == polo.TT_ID):
            if(self.Identity()):
                if(self.Chain_Call()):
                    if(self.current_tok.type == polo.TT_LPARENR):
                        self.advanceForPar()
                        if(self.Call_Args()):
                            if(self.current_tok.type == polo.TT_RPARENR):
                                self.advanceForPar()
                                if(self.listt()):
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
    
    def Call_Args(self):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type in polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or 
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL or self.current_tok.type == polo.TT_RPARENR):
            
            if(self.Identity() or self.OE() or self.current_tok.type in polo.TT_INT):
                if(self.MCall_Args()):
                    return True
            # else:
            #     return False
            return True
        else:
            return False

    #this could be a problem
    def MCall_Args(self):
        if(self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENR):
            if(self.current_tok.type == polo.TT_SEPARATOR):
                self.advanceForPar()
                if(self.Call_Args()):
                    return True
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    
    def Chain_Call(self):
        if(self.current_tok.type == polo.TT_ACESSOR or self.current_tok.type == polo.TT_LPARENR):
            if(self.current_tok.type == polo.TT_ACESSOR):
                self.advanceForPar()
                if(self.Identity()):
                    if(self.Chain_Call()):
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False

    def Dec(self):
        if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID):
            if(self.DTorID()):
                if(self.OnlyID()):
                    if(self.INIT1()):
                        if(self.listt()):
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
    
    def INIT1(self):
        if(self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_ASSIGNMENTOP or
        self.current_tok.type == polo.TT_TERMINATOR):
            if(self.current_tok.type == polo.TT_SEPARATOR):
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_ID):
                    self.advanceForPar()
                    if(self.INIT1()):
                        return True
                    else:
                        return False
                else:
                    return False
            elif(self.current_tok.type == polo.TT_ASSIGNMENTOP):
                self.advanceForPar()
                if(self.INIT2()):
                    if(self.INIT1()):
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    

    def INIT2(self):
        if(self.current_tok.type in polo.TT_INT or self.current_tok.type == polo.TT_LPARENC or self.current_tok.type == polo.TT_ID or
        self.current_tok.type == polo.TT_LPARENR or self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL or 
        self.current_tok.type == polo.TT_NEW):
            if(self.current_tok.type in polo.TT_INT):
                self.advanceForPar()
                return True
            elif(self.current_tok.type == polo.TT_LPARENC):
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
            elif(self.OE()):
                return True
            elif(self.func_call()):
                return True
            elif(self.Identity()):
                return True
            elif(self.current_tok.type == polo.TT_NEW):
                self.advanceForPar()
                if(self.INIT3()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def INIT3(self):
        if(self.current_tok.type == polo.TT_ID):
            self.advanceForPar()
            if(self.array2()):
                return True
            else:
                False
        else:
            return False
    
    def array2(self):
        if(self.current_tok.type == polo.TT_LPARENS or self.current_tok.type == polo.TT_LPARENR or self.current_tok.type == polo.TT_SEPARATOR 
        or self.current_tok.type == polo.TT_ASSIGNMENTOP or self.current_tok.type == polo.TT_TERMINATOR):
            if(self.array1()):
                return True
            elif(self.current_tok.type == polo.TT_LPARENR):
                self.advanceForPar()
                if(self.Call_Args()):
                    if(self.current_tok.type == polo.TT_RPARENR):
                        self.advanceForPar()
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    
    def more_Const(self):
        if(self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENC):
            if(self.current_tok.type == polo.TT_SEPARATOR):
                self.advanceForPar()
                if(self.current_tok.type in polo.TT_INT):
                    return True
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False

    def Assign_St(self):
        if(self.current_tok.type == polo.TT_ID):
            if(self.Identity()):
                if(self.INIT1()):
                    if(self.listt()):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def OE(self):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            if(self.AE()):
                if(self.OEe()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def OEe(self):
        if(self.current_tok.type == polo.TT_LOGICALOP  or self.current_tok.type == polo.TT_ASSIGNMENTOP or 
        self.current_tok.type == polo.TT_RPARENS or self.current_tok.type == polo.TT_RPARENR or
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_TERMINATOR):
            if(self.current_tok.type == polo.TT_LOGICALOP ):
                self.advanceForPar()
                if(self.AE()):
                    if(self.OEe()):
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False

    
    def AE(self):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            if(self.RE()):
                if(self.AEe()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def AEe(self):
        if(self.current_tok.type == polo.TT_LOGICALOP  or self.current_tok.type == polo.TT_ASSIGNMENTOP or 
        self.current_tok.type == polo.TT_RPARENS or self.current_tok.type == polo.TT_RPARENR or
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_TERMINATOR):
            if(self.current_tok.type == polo.TT_LOGICALOP ):
                self.advanceForPar()
                if(self.RE()):
                    if(self.AEe()):
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    

    def RE(self):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            if(self.E()):
                if(self.REe()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def REe(self):
        if(self.current_tok.type == polo.TT_RELATIONALOP or self.current_tok.type == polo.TT_LOGICALOP  or 
        self.current_tok.type == polo.TT_ASSIGNMENTOP or self.current_tok.type == polo.TT_RPARENS or
        self.current_tok.type == polo.TT_RPARENR or 
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_TERMINATOR):
            if(self.current_tok.type == polo.TT_RELATIONALOP):
                self.advanceForPar()
                if(self.E()):
                    if(self.REe()):
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    

    def E(self):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            if(self.T()):
                if(self.Ee()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def Ee(self):
        if(self.current_tok.type == polo.TT_PLUS or self.current_tok.type == polo.TT_MINUS or 
        self.current_tok.type == polo.TT_RELATIONALOP or self.current_tok.type == polo.TT_LOGICALOP  
        or self.current_tok.type == polo.TT_ASSIGNMENTOP or 
        self.current_tok.type == polo.TT_RPARENS or self.current_tok.type == polo.TT_SEPARATOR or
        self.current_tok.type == polo.TT_RPARENR or self.current_tok.type == polo.TT_TERMINATOR):
            
            if(self.current_tok.type == polo.TT_PLUS or self.current_tok.type == polo.TT_MINUS):
                self.advanceForPar()
                if(self.T()):
                    if(self.Ee()):
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False


    def T(self):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            if(self.F()):
                if(self.Te()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def Te(self):
        if(self.current_tok.type == polo.TT_MUL or self.current_tok.type == polo.TT_DIV or self.current_tok.type == polo.TT_MOD or
        self.current_tok.type == polo.TT_PLUS or self.current_tok.type == polo.TT_MINUS or
        self.current_tok.type == polo.TT_RELATIONALOP or self.current_tok.type == polo.TT_LOGICALOP  or 
        self.current_tok.type == polo.TT_ASSIGNMENTOP or self.current_tok.type == polo.TT_RPARENS or 
        self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENR or
        self.current_tok.type == polo.TT_TERMINATOR):
        
            if(self.current_tok.type == polo.TT_MUL or self.current_tok.type == polo.TT_DIV or self.current_tok.type == polo.TT_MOD):
                self.advanceForPar()
                if(self.F()):
                    if(self.Te()):
                        return True
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False

    def F(self):
        if(self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_INT or self.current_tok.type == polo.TT_LPARENR or
        self.current_tok.type == polo.TT_NOT or self.current_tok.type == polo.TT_BOOL):
            if(self.Identity()):
                return True
            elif(self.current_tok.type == polo.TT_INT):
                self.advanceForPar()
                return True
            elif(self.func_call()):
                return True
            elif(self.current_tok.type == polo.TT_LPARENR):
                self.advanceForPar()
                if(self.OE()):
                    if(self.current_tok.type == polo.TT_RPARENR):
                        return True
                    else:
                        return False
                else:
                    return False
            elif(self.current_tok.type == polo.TT_NOT):
                self.advanceForPar()
                if(self.F()):
                    return True
                else:
                    return False
            elif(self.current_tok.type == polo.TT_BOOL):
                return True
            else:
                return False
    
    def return_st(self):
        if(self.current_tok.type == polo.TT_RET):
            self.advanceForPar()
            if(self.OE()):
                if(self.listt()):
                    return True
                else:
                    return False
            else:
                return False
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
    
    def If_st(self):
        if(self.current_tok.type == polo.TT_IF):
            self.advanceForPar()
            if(self.current_tok.type == polo.TT_LPARENR):
                self.advanceForPar()
                if(self.OE()):
                    if(self.current_tok.type == polo.TT_RPARENR):
                        self.advanceForPar()
                        if(self.current_tok.type == polo.TT_LPARENC):
                            self.advanceForPar()
                            if(self.MST()):
                                if(self.current_tok.type == polo.TT_RPARENC):
                                    self.advanceForPar()
                                    if(self.Else_st()):
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
    
    def Else_st(self):
        if(self.current_tok.type == polo.TT_ELSE or self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or 
        self.current_tok.type == polo.TT_WHILE or self.current_tok.type == polo.TT_FOR or self.current_tok.type == polo.TT_IF or
        self.current_tok.type == polo.TT_RET or self.current_tok.type == polo.TT_RPARENC or self.current_tok.type == polo.TT_BREAK):
            if(self.current_tok.type == polo.TT_ELSE):
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_LPARENC):
                    self.advanceForPar()
                    if(self.MST()):
                        if(self.current_tok.type == polo.TT_RPARENC):
                            self.advanceForPar()
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    
    def For_st(self):
        if(self.current_tok.type == polo.TT_FOR):
            self.advanceForPar()
            if(self.current_tok.type == polo.TT_ID):
                self.advanceForPar()
                if(self.current_tok.type == polo.TT_IN):
                    self.advanceForPar()
                    if(self.current_tok.type == polo.TT_RANGE):
                        self.advanceForPar()
                        if(self.current_tok.type == polo.TT_LPARENR):
                            self.advanceForPar()
                            if(self.OE()):
                                if(self.mCond()):
                                    if(self.current_tok.type == polo.TT_RPARENR):
                                        self.advanceForPar()
                                        if(self.current_tok.type == polo.TT_LPARENC):
                                            self.advanceForPar()
                                            if(self.MST()):
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
                else:
                    return False
            else:
                return False
        else:
            return False
    

    def mCond(self):
        if(self.current_tok.type == polo.TT_SEPARATOR or self.current_tok.type == polo.TT_RPARENR):
            if(self.current_tok.type == polo.TT_SEPARATOR):
                self.advanceForPar()
                if(self.OE()):
                    return True
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False
    
    def While_st(self):
        if(self.current_tok.type == polo.TT_WHILE):
            self.advanceForPar()
            if(self.current_tok.type == polo.TT_LPARENR):
                self.advanceForPar()
                if(self.OE()):
                    if(self.current_tok.type == polo.TT_RPARENR):
                        self.advanceForPar()
                        if(self.current_tok.type == polo.TT_LPARENC):
                            self.advanceForPar()
                            if(self.MST()):
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
    
    #SSt phat rha ha
    def SST(self):
        if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_WHILE or
        self.current_tok.type == polo.TT_FOR or self.current_tok.type == polo.TT_IF or self.current_tok.type == polo.TT_RET or
        self.current_tok.type == polo.TT_BREAK):
            if(self.func_call()):
                return True
            elif(self.Dec()):
                return True
            elif(self.While_st()):
                return True
            elif(self.For_st()):
                return True
            elif(self.If_st()):
                return True
            elif(self.Assign_St() ):
                return True
            elif(self.return_st()):
                return True
            elif(self.break_st()):
                return True
            else:
                return False
    
    def MST(self):
        if(self.current_tok.type == polo.TT_DT or self.current_tok.type == polo.TT_ID or self.current_tok.type == polo.TT_WHILE or
        self.current_tok.type == polo.TT_FOR or self.current_tok.type == polo.TT_IF or self.current_tok.type == polo.TT_RET or
        self.current_tok.type == polo.TT_BREAK or self.current_tok.type == polo.TT_RPARENC):
            if(self.SST()):
                if(self.MST()):
                    return True
                else:
                    return False
            # else:
            #     return False
            return True
        else:
            return False


    # def factor(self):
    #     tok = self.current_tok.type

    #     if tok.type in (polo.TT_INT , polo.TT_FLOAT, polo.TT_ID):
    #         self.advanceForPar()
    #     return nodes.NumberNode(tok)
    
    # def term(self):
    #     return self.bin_op(self.factor, (polo.TT_MUL, polo.TT_DIV, polo.TT_MOD))

    # def expr(self):
    #     return self.bin_op(self.term, (polo.TT_PLUS, polo.TT_MINUS))
    
    # def Rel_expr(self):
    #     return self.bin_op(self.expr, (polo.TT_RELATIONALOP))
    
    # def And_expr(self):
    #     return self.bin_op(self.Rel_expr, (polo.TT_LOGICALOP))
    
    
    # def bin_op(self, func, ops):
    #     left = func()

    #     while self.current_tok.type.type in ops:
    #         op_tok = self.current_tok.type
    #         self.advanceForPar()
    #         right = func()
    #         left = nodes.BinOpNode(left, op_tok, right)
        
    #     return left