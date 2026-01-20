import numpy as np

#broadcasting  : 
#rules : 
'''
1. - matching dimentions : [1,2,3]+[4,5,6]=[5,7,9]
2. - expanding element : [1,2,3]+10=[11,12,13]
3. - incompatible shape : [1,2,3]+[1,2]=Value error 
'''
price=np.array([100,200,300,400])
discount=10
final_prices=price-(price*discount/100)
print(final_prices)

arr=np.array([10,20,30])
arr1=np.array([5,10])
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([10,20,30])

#single array : 
result=arr * 2
print(result)

# 1d to 2d array
print(arr2+arr3)

#Value error:
print(arr+arr1)



