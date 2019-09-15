import polo

while True:
    text = input('POLO > ')
    result, error = polo.run(text)

    if error: 
        print(error.as_string())
    else:
        for i in result:
            print('[value:' ,i.value ,'| Type: ' + i.type,']')

# import basic

# while True:
#     text = input('basic > ')
#     result, error = basic.run('<stdin>', text)

#     if error: print(error.as_string())
#     else: print(result)