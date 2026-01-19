import numpy

#shape

arr_2d=numpy.array([[23,34,56],
                   [45,87,57]])
# print(arr_2d)
print(arr_2d.shape)
#output = (2,3)--> 2: rows,3:columns

arr1=numpy.array([1,2,3])
arr2=numpy.array([[1,2,3],[2,4,5]])
arr3=numpy.array([[[1,2,3],[2,4,5],[5,6,7]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
#output : 
# 1:1d array,2:2d array,3:3d array

#data type of array : 

datatype=numpy.array([10,45,78,4.5])
print(datatype.dtype)

arr4=numpy.array([4.8,5.0,9.7,8.9])
print(arr4.dtype)
intarr=arr4.astype(int)
print(intarr)

#mathamatical operation : 

maths=numpy.array([10,20,30])
print(maths+10)
print(maths**2)
print(maths)

list=numpy.array([2,35,54,343,56])
print(numpy.sum(list))
print(numpy.min(list))
print(numpy.max(list))
print(numpy.mean(list))
print(numpy.std(list))

