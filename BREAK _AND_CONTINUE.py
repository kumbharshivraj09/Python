#BREAK : TO STOP THE LOOP 

'''num=int(input('enter a number : '))
list=[]

for n in range(1,num+1):
    if n==22:
        break
    list.append(n)
    
print(list)    

num=int(input('enter a number : '))
list=[]

for n in range(1,num+1):
    if n%2==0:
        continue
    list.append(n)
    
print(list) '''


user=['rohan','shivraj','rohit','ram','sham','rahul']
name=''

while True:
    name=input("enter your name : ")
    if name=='exit':
        break
    elif name in user:
        print('name already exist!')
    else:
        print(name)    

