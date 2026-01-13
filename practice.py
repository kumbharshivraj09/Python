# count even and odd numbers in a list : 

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