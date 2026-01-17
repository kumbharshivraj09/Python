'''# count even and odd numbers in a list : 

list=[1,45,58,66,5,2,8,6,66,23,11,10,102,12,20,3,30,0]

even=odd=0
for i in list:
 if i%2==0:
    even+=1
 else:
    odd+=1

print("even : ",even)     
print("odd : ",odd)     



#reverse string : 

s=input(" enter a string : ")
print(s[::-1])


#prime number : 

num=int(input("enter a number : "))

if num>1:
  for i in range(2,num):
    if num%i==0:
      print("not prime! ")
      
    else:
      print("prime")
      break
else:
  print("not prime!")


 # factorial number : 

num=int(input("enter a number : ")) 

factorial=1

if num<0:
    print("sorry , factorial is not negative!!!")
elif num==0:
    print("factorial of 0 is : 1")

else:
    for i in range(1,num+1):
        factorial=factorial*i
print(f'factorial of {num} is : {factorial}')  

#sum of all number : 

def sum(*numbers):
    total=0
    for i in numbers:
      total+=i
      return total
    
print(sum(2,283,9404,48,9))  '''


'''def string_test(s):
    d={"UPPER":0,"lower":0}

    for i in s:
        if i.isupper():
            d["UPPER"]+=1

        elif i.islower():
           d["lower"]+=1
        else:
            pass

    print("original string is : ",s)
    print("number of upper case character is : ",d["UPPER"])            
    print("number of lower case character is : ",d["lower"])   



string_test("ROHIT shinde KOLHAPUR maharashtra")   '''




