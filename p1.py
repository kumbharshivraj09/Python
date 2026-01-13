#fizzbuzz game 
#fizz : num%3==0
#buzz : num %5==0
#fizzbuzz : num%3and5==0

num=int(input("enter a number : "))
mylist=[]
for n in range(1,num+1):
   result=""
   if n%3==0:
    result=result+"fizz"
    if n%5==0:
      result=result+'buzz'
   elif n%5==0:
     result=result+'buzz'
   else:
     result=n  
   mylist.append(result)
print(mylist)  
