import Class_Data_Table as CDT

class ClassTable:

    CT_List = []


    name = ""
    type_ = "class"
    Parent = ""
    CDT_ref = CDT.ClassDataTable()
    
    def lookUp_CT(self, N):
        for i in self.CT_List:
            if(i.name == N):
                print("name found")
                return i.name


    def Insert_CT(self, N, P):
        temp = ClassTable()
        temp.name  = N
        temp.Parent = P
        temp.CDT_ref = CDT.ClassDataTable()

        chk = temp.lookUp_CT(temp.name)
        
        if(chk == None):
            self.CT_List.append(temp)
            print(temp.name + " inserted in class table" , temp.Parent)
        else:
            print("ReDeclaration error")

    def Ret_ClassObj(self, CN):
        for i in self.CT_List:
            if(i.name == CN):
                print(i.name + " exists")
                return i
    
    def Insert_CDT(self,CN, N, T, AM):
        classObj = self.Ret_ClassObj(CN)
        classObj.CDT_ref.Insert_CDT2(N, T, AM)
    
    def LookUp_CDT(self,CN ,N): #, T, AM
        classObj = self.Ret_ClassObj(CN)
        if(classObj):
            return classObj.CDT_ref.LookUp_CDT2(N)
        else:
            return None
    
    def lookUpFunc_CDT(self, CN,N, AL):
        classObj = self.Ret_ClassObj(CN)
        return classObj.CDT_ref.lookUpFunc_CDT2(N, AL)
    
    def Print_CT(self):
        for i in self.CT_List:
            print("class name: " + i.name + " type: " + i.type_ + " Parent: " + i.Parent)
            print("\n")
            i.CDT_ref.Print_CDT()

# c = ClassTable()
# c.Insert_CT("faraz", "null")
# c.Insert_CDT("faraz", 'a', 'int', 'public')
# c.Insert_CDT("faraz", 'a', 'float', 'public')
# c.Print_CT()

# f = c.Ret_ClassObj("faraz")
# print(f.name + f.Parent) 
# print(f.CDT_ref)

