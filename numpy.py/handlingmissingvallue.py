import numpy as np

#Handling Misssing Value : 
#built in function : np.isnan-->detect missing value
# np.nn_to_num,np.isinf


#np.isnan:
arr=np.array([10,np.nan,33,np.nan,38,3949])
print(arr)
print(np.isnan(arr))

#np.nan_to_num

print(np.nan_to_num(arr))#defoult 0
print(np.nan_to_num(arr,nan=100))

#np.idinf : 

arr1=np.array([1,10,np.inf,20,29,-np.inf])
print(arr1)
print(np.isinf(arr1))

#replace
print('replace')
print(np.nan_to_num(arr1,posinf=1000,neginf=-1000))