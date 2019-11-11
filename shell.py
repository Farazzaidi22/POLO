import polo

# while True:
#     text = input('POLO > ')

with open('commands.txt', 'r') as filee:
    text = filee.read()
# print(text)

result, error = polo.run(text)   
if error: print(error.as_string()) 

else: print(result)
# else:   
#      for i in result:
#          print('[value:' ,i.value ,'| Type: ' + i.type,']')

# import basic2

# # while True:
# #     text = input('basic > ')
# with open('commands.txt', 'r') as filee:
#     text = filee.read()
# result, error = basic2.run('<stdin>', text)
# if error: print(error.as_string())
# else: print(result)