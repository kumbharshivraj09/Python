import numpy as np

#reshaping : 
arr=np.array([10,20,30,40,50,60])
reshape=arr.reshape(2,3)
print(reshape)

# flatiing
# ravel : views return
# flatten : copy return
# flatting is use for when you want convert md array into 1d array
# 

arr2=np.array([[12,34,45],[2,34,45]])
print(arr2.ravel())
print(arr2.flatten())