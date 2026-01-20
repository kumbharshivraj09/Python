import numpy as np
# stacking : 
'''
vertically stack
horizonally stack

vstack()-->row wise
hstack()-->column wise
'''
arr1=np.array([1,2,3,4,5,7])
arr2=np.array([2,0,8,9,5,8])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

# spliting :

print(np.split(arr1,2))
print(np.split(arr1,3))


