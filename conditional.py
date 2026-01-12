# IF-ELSE : 

'''age=int(input("enter a age : "))
if age>18:
    print("you can vote!")
else:
    print("you can not vote!")

num=int(input("enter number :"))
if num%2==0:
    print("number is even ")
else:
    print("number is odd ")'''

# list=['rohit',8,'a','b']

# if 'a' in list:
#     print('a in list')
# else:
#     print("a is not in list ")


#EL-IF - 

'''mark=int(input("enter your mark : "))
if mark>=90 and mark<=100:
    print("a+ grade ")
elif mark>=80 and mark<90:
    print('a grade')
elif mark>=60 and mark<80:
    print('b+ grade')
elif mark>=40 and mark<60:
    print('b grade')   
else:
    print("fail") '''

# if-else nesting : 

age = int(input("enter your age : ")) 
voter_id=input("enter voter id true or false : ")  
 
if age>18:
    if voter_id=='true':
        print("you can applied for vote!")
    else:
        print("you can not applied for vote!")
    
else:
    print("you can not vote!")