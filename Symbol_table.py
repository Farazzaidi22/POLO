# import Extra_function as EF

class SymbolTable:

    ST_List = []


    name = ""
    type_ = ""
    scope = None
    
    def lookUp(self, N, S):
        for i in self.ST_List:
            if(i.name == N and i.scope == S):
                print("name found")
                return i.type
            # else:
            #     print("not declared")
            #     return None
    
    def lookUp_fun(self, N, AL):
        for i in self.ST_List:
            if(i.name == N and i.type == AL):
                print("name found")
                return i.type
    
    # def match_list(self, AL):
    #     for i in self.ST_List:
    #         while(self.ST_List != None)
    #         if(i.type == AL):
    #             rt = EF.Compatibility(AL, i.type, None)
            


    def Insert_ST(self, N, T, S):
        temp = SymbolTable()
        temp.name  = N
        temp.type  = T
        temp.scope = S

        chk= temp.lookUp(temp.name, temp.scope)
        
        if(chk == None):
            self.ST_List.append(temp)
            print(temp.name + " is inserted in symbol table")
        else:
            print("ReDeclaration error")


