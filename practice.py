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

# write a program to convert two list into dictionary
def list_to_dic():
 keys=[1,2,3]
 values=['one','two','three']
 result=dict(zip(keys,values))
 print(result)


def dic_to_touple():
   x={1:'one',2:'two',3:'three'} 
   for i in x.items():
      print(i)

list_to_dic()
dic_to_touple()

# find the missing number in array
def get_missing_no(a):
   n=a[-1]
   total=n*(n+1)/2
   sum1=0
   sum1=sum(a)
   result=total-sum1
   print("Missing Number is :",int(result))
   
a=[1,2,3,4,5,6,8,9,10]   
get_missing_no([1,2,3,4,5,6,8,9,10])
