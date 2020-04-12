Label_stack = []
Label_no    = 0 
T = 0
F = 0

file1 = open("ICG_Output.txt","w")

def StartLabel():
    global Label_no, Label_stack
    Label_stack.append(Label_no)
    file1.write("L")
    e = str(Label_no)
    file1.write(e)
    file1.write("_start: \n")
    Label_no += 1

def manage_Cod():
    file1.write("if (T")
    global T 
    a = T
    b = str(a)
    file1.write(b)
    file1.write(" == false) jmp ")
    
    e = Label_no
    e -= 1
    f = "L"+ str(e) +"_finish"
    file1.write(f)
    
    file1.write(" \n")
    T += 1

def manage_st(t1, t2, OP):
    s1 = str(t1)
    s2 = str(t2)
    s3 = str(OP)
    
    a = T
    b = str(a)
    file1.write(b)
    
    file1.write(" " + s1 + " " + s3 + " " + s2)
    file1.write(" \n")
    T += 1



def FinishLabel():
    s_no = Label_stack.pop()
    if(Label_stack != None):

        file1.write("L")
        
        e = str(s_no)
        
        file1.write(e)
        file1.write("_finish: \n")
    else:
        return -1
