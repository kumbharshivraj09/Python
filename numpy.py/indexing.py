import numpy as np

#indexing : 
arr=np.array([10,20,30,40,50,60])
#numpy follow 0 index : 
print(arr[0])#first element
print(arr[2])#third element
print(arr[-1])#last element

#slicing
print(arr[0:4])
print(arr[:3])
print(arr[3:])

print(arr[::2])
print(arr[::-1])
print(arr[1::2])

#fancy indexing : 
# selecting multiple element at once :

print(arr[[0,3,4]])

# filtering data :
print(arr[arr<25])
print(arr[arr>25])
