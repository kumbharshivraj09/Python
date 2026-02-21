import pandas as pd 
import numpy  as np
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_csv('financial.csv')
print(df.head(2))

# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df.dtypes)

print(df.isna().sum())
print(df.columns)

print(df['R&D_Spending_USD_Mn'].sum())

print(df['Company'].unique())
#convert date coulumn dataype obj to datetime
print(df['Date'].dtype)
df['Date']=pd.to_datetime(df['Date'])
print(df['Date'].dtype)

#create new column for year only
df['Year']=df['Date'].dt.year
print(df.head(1))

#how much amount the company spend to r&d
# RD=df.groupby('Company')['R&D_Spending_USD_Mn'].sum()/1000
# print(RD)
# plt.bar(RD.index,RD.values,color=['lightgreen','skyblue','orange'])
# plt.ylabel("AMOUNT IN BILLIONS DOLLAR")
# plt.xlabel("COMPANY")
# plt.title("R&D SPENDING BY THE COMPANIES ")

# plt.show()

# #revenue earned by the companies 
# revenue=df.groupby('Company')['AI_Revenue_USD_Mn'].sum()/1000
# print(revenue)
# plt.bar(revenue.index,revenue.values,color=['red','green','yellow'])
# plt.ylabel("REVENUE IN BILLION DOOLAR")
# plt.xlabel('COMPANY')
# plt.title("REVENUE EARNED BY THE COMPANIES ")
# plt.show()

# #USE SUBPLOT FOR REVENUE AND R&d
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.bar(RD.index,RD.values,color=['lightgreen','skyblue','orange'])
# plt.ylabel("AMOUNT IN BILLIONS DOLLAR")
# plt.xlabel("COMPANY")
# plt.title("R&D SPENDING BY THE COMPANIES ")
# plt.subplot(1,2,2)
# plt.bar(revenue.index,revenue.values,color=['red','green','yellow'])
# plt.ylabel("REVENUE IN BILLION DOOLAR")
# plt.xlabel('COMPANY')
# plt.title("REVENUE EARNED BY THE COMPANIES ")
# plt.show()

#date wise impact on the stock
# plt.figure(figsize=(20,5))
# plt.tight_layout()
# print(df['Stock_Impact_%'])
# plt.plot(df['Date'].head(20),df['Stock_Impact_%'].head(20),)
# plt.show()

#create 3 seperate dataframe for company 
openai=df[df['Company']=='OpenAI']
print(openai)

openai=df[df['Company']=='OpenAI']
print(openai)

Google=df[df['Company']=='Google']
print(Google)

Meta=df[df['Company']=='Meta']
print(Meta)

plt.figure(figsize=(10,5))
plt.tight_layout()
plt.plot(openai['Date'],openai['Stock_Impact_%'],color='red')
plt.show()


plt.figure(figsize=(10,5))
plt.tight_layout()
plt.plot(Meta['Date'],Meta['Stock_Impact_%'],color='blue')
plt.show()


plt.figure(figsize=(10,5))
plt.tight_layout()
plt.plot(Google['Date'],Google['Stock_Impact_%'],color='green')
plt.show()





#event when maximum stock impact was observed
