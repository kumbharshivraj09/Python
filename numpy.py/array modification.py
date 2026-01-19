import numpy as np
#  insert : 
arr=np.array([20,10,30,40,50,60])
print(arr)
print(np.insert(arr,3,70))

arr2d=np.array([[1,2],[3,4]])
print(arr2d)
print(np.insert(arr2d,1,[8,9],axis=0))
print(np.insert(arr2d,1,[8,9],axis=1))
print(np.insert(arr2d,1,[8,9],axis=None))


#  add : 

print(np.append(arr,[1,2,3]))

# concating : 
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,3])
arr3=np.concatenate((arr1,arr2),axis=0)
print(arr3)

#delete : 

print(arr)
print(np.delete(arr,0))
print(np.delete(arr,[1,2]))
print(np.delete(arr2d,0,axis=0))#delete 2d array
