#modify data : 
# 1- update 2-add column 3-remove

import pandas as pd

data={
    "name":["rahul",'sagar','karan','ajay','omkar'],
    'age':[22,36,20,20,21],
    'city':['pune','nagpur','kolhapur','sangali','satara']
}

df=pd.DataFrame(data)
print(df)

#using insert : 

#syntax:
#df.insert(loc,column_name,[some data])

df.insert(3,"sallary",[40000,50000,55000,68000,72000])
print(df)

df["bonus"]=df["sallary"]*0.1
print(df)

#updating values : 

# syntax:
# df.loc[row index,column name]=new value
df.loc[2,'sallary']=85000
print(df)

#incrising sallary by 5%

df["sallary"]=df["sallary"]*1.05
print(df)

#removing columns : 

df.drop(columns=["bonus",'age'],inplace=True)
print(df)

#handling missing data : 

#NaN - not a number 
#null(for object data type )

#isnull() method
#return true or false 

