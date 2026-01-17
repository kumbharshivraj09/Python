import pandas as pd
#handling missing data : 

#NaN - not a number 
#null(for object data type )

#isnull() method
#return true or false 
#true - value missing
#false - value present

data={
    "name":["rahul",'shyam','karan','ajay','omkar'],
    'age':[22,None,20,20,21],
    'city':['pune','nagpur','kolhapur','sangali','satara']
}

df=pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())

#handle missinng values : 
#dropna()

#axis=0 : rows 
#axis=1 : columns

# df.dropna(inplace=True)
# print(df)

# df.fillna(0,inplace=True)
# print(df)

df['age'].fillna(df["age"].mean(),inplace=True)
print(df)