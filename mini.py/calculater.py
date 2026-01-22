history_file='HISTORY.txt'

def show_histtory():
    file=open('HISTORY.txt','r')
    lines=file.readlines()
    if len(lines)==0:
        print("NO History Found!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open('HISTORY.txt','w')
    file.close()

    print("History Closed!")

def save_history(equation,result):
    file=open('HISTORY.txt','a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculater(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("Invalid Input.Use Format : number operator number (eg.8 + 9)")
        return
    
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])

    if op=="+":
        result=num1+num2

    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
        if num2==0:
            print("cannot divide by zero!")
            return
        result=num1/num2
    else:
        print("Invalid operator. USE ONLY + - * /")
        return
    
    if int(result)==result:
       result==int(result)
    
    print("RESULT : ",result)
    save_history(user_input,result)
def main():
    print("____SIMPLE CALCULATION(+ - * /) or Command (history,exit,clear)")
    while True:
        user_input=input("enter a calculation (+ - * /) or command ((history,exit,clear)")
        if user_input=='exit':
            print('GOODBYE!')
            break
        elif user_input=='history':
            show_histtory()
        elif user_input=='clear':
            clear_history()

        else:
            calculater(user_input)
main()                





