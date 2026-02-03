import numpy as np
 

# basics numpy
arr=np.array([1,2,3])#1d array
print(arr)
print(arr.dtype)
print(arr.ndim)

arr1=np.array([[1,2,3],[1,23,55]])#2d array
print(arr1)

# list vs numpy
list=[1,2,3]
print(list*2)#outpupt:[1, 2, 3, 1, 2, 3]
print(arr*2)#output:[2 4 6]

# creating array from srcath: 
zero=np.zeros((2,3))
print("zero array : ",zero)

one=np.ones((2,3))
print("ones array : ",one)

full=np.full((2,4),11)
print(full)

full=np.full((2,4),'fruit')
print(full)

random=np.random.random((2,2))
print(np.random.randint(random))

rang=np.arange(0,18,3)
print(rang)

# vector,matrix,tensor

vector=np.array([1,2,3,3])
print("Vector : ",vector)

matrix=np.array([[1,2],[3,4]])
print("Matrix : ",matrix)

tensor=np.array([[[1,2],[3,4],[5,6],[7,8],[9,0]]])
print("Tensor : ",tensor)

# Array Properties : 
array=np.array([[1,2,3],[4,5,6]])
print(array)
print(array.shape)
print(array.ndim)
print(array.dtype)
print(array.size)

# Array Reshaping : 

array=np.array([[1,2,3],[4,5,6]])
print("orignal array : ",array)

reshape=array.reshape((3,2))
print("Reshape array : ",reshape)

flateld=reshape.flatten()
print("flattened array : ",flateld)

# ravel return views instead copy and orignal array is safe
raveld=reshape.ravel()
print("raveld array : ",raveld)

# phase 2 of numpy

# numpy array operation : 
#1d arry
array1d=np.array([1,2,3,4,5,6,78,8])
print("basic slicing : ",array1d[1:8])
print("negative indexing : ",array1d[-4])
print("step : ",array1d[2:8:2])

# 2d array 
arr2d=np.array([[1,2,3],[2,45,6]])
print("specific element : ",arr2d[1,2])
print("entire row : ",arr2d[1])
print("entire column : ",arr2d[:,1])


#sorting : 
array=np.array([2,5,7,134,1,56,54,23])
print("sorted array : ",np.sort(array))

# 2d array dort : 
array2d=np.array([[3,5,7],[2,1,4],[9,0,12]])
print("sorted 2d array by columns : ",np.sort(array2d,axis=0))
print("sorted 2d array by rows : ",np.sort(array2d,axis=1))

# filtering : 
numbers =np.array([1,2,3,4,5,6,7,8,9,10])
evenno=numbers[numbers%2==0]
print("even number : ",evenno)

# filter with mask : 
mask=numbers%2==0
print("even number : ",numbers[mask])

# fancy indexing : 
print("fancy indexing : ",numbers[[0,1,5]])

np_where=np.where(numbers>5)
print("numpy where : ",numbers[np_where])

# conditional : 
condition=np.where(numbers>5,numbers*5,numbers)
print("condition array : ",condition)

# adding and removing data : 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

# combine
arr3=np.concatenate((arr1,arr2))
print(arr3)

# compatibility shape : 
print("compatibility shape is : ",arr1.shape==arr2.shape)
print("compatibility shape is : ",arr1.shape==arr3.shape)

# vstack : 
orignal=np.array([1,2,5,6])
newrow=np.array([1,2,3,4])
print("using vstack : ",np.vstack((orignal,newrow)))
print("using hstack : ",np.hstack((orignal,newrow)))

# delete

arr=np.array([1,2,3,4,5,9])
print(np.delete(arr,2))

# add
print(np.append(arr,[11,12]))




