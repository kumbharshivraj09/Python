

# print(10+5)
# print(5-55)
# try:
#     print(5/0)
# except Exception as e:
#     print(e,type(e))    

# print(2*88)    


try:
 with open ('user_ino.txt','r') as file:
    content=file.readlines()
    print(content)
except Exception as e:
    print(e,type(e))
else:    
 for line in content:
    print(f'wellcome {line.rstrip()}')
try:
 with open ('user_info.txt','r') as file:
    content=file.readlines()
    print(content)
except Exception as e:
    print(e,type(e))
else:    
 for line in content:
    print(f'wellcome {line.rstrip()}')
