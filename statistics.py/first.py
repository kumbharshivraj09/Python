import pandas as pd
import numpy as np

data={"name":["rohan","rohit","sourabh","sahi","shreyash","shravan"],
      "marks":[89,76,89,90,52,85]}
data1={"name":["gururaj","shubham","sujal","parth","vaibhav","rupesh"],
       "marks":[88,87,90,89,97,70]}

df1=pd.DataFrame(data)
print(df1)
df2=pd.DataFrame(data1)
print(df2)

# print(df1.describe())
# print(df2.describe())

print(df1["marks"].mode())#mode
print(df2["marks"].mode())#mode here no any value double

print(df1["marks"].mean())#mean
print(df2["marks"].mean())#mean

# in meadian first sort the data and if value is odd select 
# middel value else value is even select middle 2 value and calculate avg to the 2 value
print(df1["marks"].median())#meadian 
print(df2["marks"].median())#meadian

# std

print(df1["marks"].std())#standard deviation
print(df2["marks"].std())#standard deviation

# variance
print(df1["marks"].var())#variance
print(df2["marks"].var())#variance

# mean absolute value
mean=df1["marks"].mean()
deviation=df1["marks"]-mean#marks-mean
abs_deviation=deviation.abs()
mad=abs_deviation.mean()
print(mad)

