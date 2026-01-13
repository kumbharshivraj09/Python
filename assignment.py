def calculator():
    num1=int(input("enter first number : "))
    num2=int(input("enter second number : "))

    while True: 
     print('\n+')
     print('-')
     print('*')
     print('/')

     op=input("enter a operator : ")
     if op=='+':
        result=num1+num2
     elif op=='-':
        result=num1-num2
     elif op=='*':  
        result=num1*num2
     elif op=='/':
        if num2==0:
           print("error : division by zero!")
           continue
        result=num1/num2
     else:
        print('invalid operator!!!')
     print(f'result of {num1} {op} {num2} is : {result}')
     choice =input(f'continnue operation with {result}? y/n  ').lower()    
     if choice=='y':
       num1=result
       num2=int(input("enter a number : "))
       
     else:
       print("calculator closed!!!!")



calculator()