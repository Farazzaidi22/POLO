# # Search function with parameter list name 
# # and the value to be searched 
# def search(list,n): 
  
#     for i in range(len(list)): 
#         if list[i] == n: 
#             return True
#     return False
  
# # list which contains both string and numbers. 
# list = ['int', 'float'] 
  
# # Driver Code 
# n = 'int'
  
# if search(list, n): 
#     print("Found") 
# else: 
#     print("Not Found") 

# def amil(self):
#         while self.current_char != None and "\"":
#             qc = 0
#             if self.current_char == "\"":
#                 qc += 1
        
#         if qc % 2 = 0:
#             return False
#         elif qc % 2 > 0:
#             return True

# import itertools  
  
# num = [1, 2, 3] 
# color = ['red', 'while', 'black'] 
# value = [255, 256] 
  
# iterates over 3 lists and excutes  
# 2 times as len(value)= 2 which is the 
# minimum among all the three  
# for (a, b, c) in zip(num, color, value): 
#      print(a, b, c) 
  
# print("\niterating using izip")
# for (a, b, c) in itertools.izip(num, color, value): 
#     print(a, b, c)

# a = ['a1', 'a2', 'a3']
# b = ['b1', 'b2']

# print ("List comprehension:")
# for x, y in [(x,y) for x in a for y in b]:
#     print (x, y)

# def tryy(a):
#     print("hello amil" + a)

# def tryy(a):
#     print(a + 1)


# tryy(5)

# Program to show various ways to read and 
# write data in a file. 
file1 = open("myfile.txt","w") 
L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
  
# \n is placed to indicate EOL (End of Line) 
file1.write("Hello \n") 
# file1.writelines(L) 
file1.close() #to change file access modes 
  
# file1 = open("myfile.txt","r+")  
  
# print("Output of Read function is ")
# print(file1.read())
# # print
  
# # seek(n) takes the file handle to the nth 
# # bite from the beginning. 
# file1.seek(0)  
  
# print ("Output of Readline function is ")
# print (file1.readline()) 
# # print
  
# file1.seek(0) 
  
# # To show difference between read and readline 
# print ("Output of Read(9) function is ")
# print (file1.read(9)) 
# # print
  
# file1.seek(0) 
  
# print ("Output of Readline(9) function is ")
# print (file1.readline(9)) 
  
# file1.seek(0) 
# # readlines function 
# print ("Output of Readlines function is ")
# print (file1.readlines()) 
# # print
# file1.close() 