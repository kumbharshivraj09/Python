import pandas as pd 
import numpy as np
#from sklearn

#handling missinng data

df={
    'Name':['rahul','rohit','sumit','vivek'],
    'Age':[None,25,35,None],
    "Sallary":[45000,55200,None,60000]
}
data=pd.DataFrame(df)
print(data)

print(data.isna().sum())
# print(data.dropna())
data["Age"]=data['Age'].fillna(data['Age'].mean())
data["Sallary"]=data['Sallary'].fillna(data['Sallary'].mean())
print(data)

