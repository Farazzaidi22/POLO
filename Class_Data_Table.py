class ClassDataTable:
    name = ""
    type_ = ""
    AM = ""
    Class_Data_List = []


    def __init__(self):
        self.name  = None
        self.type_ =  None
        self.AM    = None
        self.Class_Data_List = []


    def LookUp_CDT2(self, N):
        for i in self.Class_Data_List:
            if(i.name == N):
                print(i.name + " exists")
                return i.type_
    
    def lookUpFunc_CDT2(self, N, AL):
        for i in self.Class_Data_List:
            if(i.name == N and i.type_ == AL):
                print("name found")
                return i.type_
    
    def Insert_CDT2(self, N,T,AM):
        chk = self.LookUp_CDT2(N)
        
        if(chk == None):
            temp = ClassDataTable()
            temp.name  = N
            temp.type_ = T
            temp.AM    = AM
            self.Class_Data_List.append(temp)
            print(temp.name + " inserted in class Data table")
        else:
            print("ReDeclaration error")
        

    
    def Print_CDT(self):
        for i in self.Class_Data_List:
            print("var: " + i.name + " type: " + i.type_ + " Acess Mod: " + i.AM)
    
# t1 = ClassDataTable()
# t1.Insert_CDT2("faraz", "string", "public")

