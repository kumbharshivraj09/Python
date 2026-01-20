import numpy as np

# vectorization : 

# using for loop

list1=[1,2,3]
list2=[4,5,6]

result=[x+y for x,y in zip(list1,list2)]#list comprehention
print(result)

#using vectorization (numpy): it is 100* faster than loop

arr1=np.array([1,2,3])
arr2=np.array([5,6,7])
print(arr1+arr2)

