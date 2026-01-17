import pandas as pd 
data={
    "custmer_id":[1,2,4,6],
  "name":['ram','shyam','karan','rohit'],
}
df=pd.DataFrame(data)
data={
    "custmer_id":[1,8,4,7],
  "order amount":[20,99,360,145454],
}

dataorder=pd.DataFrame(data)


print(pd.merge(df,dataorder, on="custmer_id",how="inner"))

print(pd.merge(df,dataorder, on="custmer_id",how="outer"))
print(pd.merge(df,dataorder, on="custmer_id",how="left"))
# print(pd.merge(df,dataorder, on="custmer_id",how=""))
print(pd.merge(df,dataorder, on="custmer_id",how="right"))
