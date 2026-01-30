#function : 
#      1.  function is a block of code 
#      2.  which perform some task
#      3.  run when it is called


num1=int(input(" enter first number :  "))
num2=int(input(" enter second number :  "))

def add(num1,num2):
    sum=num1+num2
    return sum
result=add(num1,num2)

def sub(num1,num2):
    subt=num1-num2
    return subt

def multi(num1,num2):
    mult=num1*num2
    return mult

def div(num1,num2):
    divi=num1/num2
    return divi

result=add(num1,num2)
resul=sub(num1,num2)
resu=multi(num1,num2)
res=div(num1,num2)

print("addtition of two number is : ",result)
print("subtraction of two number is : ",resul)
print("multiplication of two number is : ",resu)
print("divison of two number is : ",res)



# def greatting(username,*hobbies):
#     print('*'*17)
#     print(f'well come {username}')
#     print('thank you for sign in')
#     print('*'*17)
#     print("hobby are :")

#     for hobby in hobbies:
#         print(hobby)
# greatting('raju','singing','playing','swiming')    
# greatting('babu','dancing','playing')    
# greatting('kumar','crying','swiming')    
# greatting('ram','listing','sleeping')    

# def greatting(username,**user_info):
#      print('*'*17)
#      print(f'well come {username}')
#      print('thank you for sign in')
#      print('*'*17)
#      for key,value in user_info.items():
#        print(f'{key } is {value}')
# greatting('raju',age=15,city='kolhapur')    
# greatting('babu',age=45,city='pune')    
# greatting('kumar',age=29,city='kolhapur')    
# greatting('ram')    


# write a program to find common letters bettwwen two strings
def common():
    str1=input("enter a first letter : ")
    str2=input("enter a second letter : ")
    s1=set(str1)
    s2=set(str2)
    print(s1)
    print(s2)
    common_letter=s1 & s2
    print('Common Letter is : ',common_letter)

common()  

# write a program  the frequency of words appearing in a string

def frequency():
    str=input("enter a string : ")
    list=str.split()
    d={}
    for i in list:
      if i not in d.keys():
         d[i]=0
      d[i]=d[i]+1
    print(d)
frequency()    



