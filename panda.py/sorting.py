import pandas as pd 
data={
  "name":['rahul',"rohit",'ram','pavan','shubham'],
  "age":[45,25,26,35,85],
  "sallary":[11000,55000,45123,85026,62100]
 }
df=pd.DataFrame(data)
print(df)

df.sort_values(by="age",ascending=True,inplace=True)
print(df)

df.sort_values(by=["age","sallary"],ascending=[True,False],inplace=True)
print(df)