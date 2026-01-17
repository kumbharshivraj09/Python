import pandas as pd 
data={

    'time' : [2,4,5,7,9],
    "value":[10,None,None,40,None]
}

print("before interpolution!")
df=pd.DataFrame(data)
print(df)

df["value"]=df["value"].interpolate(method="linear")
print("after interpolution!!!")
print(df)