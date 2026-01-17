import pandas as pd 
data={
  "name":['rahul',"rohit",'ram','pavan','shubham'],
  "age":[45,25,25,35,85],
  "sallary":[11000,55000,45123,85026,62100]
 }
df=pd.DataFrame(data)
print(df)
print(df['sallary'].mean())
print(df['sallary'].min())
print(df['sallary'].max())
print(df['sallary'].median())



#grouping in pandas : 
group=df.groupby("age")["sallary"].sum()
print(group)

#multiplay grouping : 

group=df.groupby(["age","name"])["sallary"].sum()
print(group)
