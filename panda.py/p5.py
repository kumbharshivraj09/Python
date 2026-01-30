import pandas as pd 
import numpy as np

df=pd.read_csv('googleplaystore.csv')
print(df.head())
print(df.shape[0])
print(df.shape[1])
print(df.columns)

# get total number of app titles contain astrology
print(df['App'])
print(len(df[df['App'].str.contains(' Astrology',case=True)]))

# find average app rating
print(df["Rating"].mean())

# find total number of unique category
print(df['Category'].nunique())

# which category getting the highest avg rating
print(df.groupby('Category')['Rating'].mean())

# find the total number of apps having 5stars rating
print(len(df[df['Rating']==5.0]))

# find the avg value of reviews
print(df['Reviews'].dtype)
# print(df['Reviews'].astype('float'))
df['Reviews']=df['Reviews'].replace('3.0M',3.0)
df['Reviews']=df['Reviews'].astype('float')

print(df['Reviews'].dtype)
print(df['Reviews'].mean())

# find the total number of free and paid app
print(df.columns)
print(df['Type'].value_counts())

# which app has max reviews
print(df[df['Reviews'].max()==df['Reviews']]['App']) 

# display top 5 app having highest reviews

index=df['Reviews'].sort_values(ascending=False).head().index
print(df.iloc[index]["App"])

# find the avg rating of free and  paid apps 
print(df.groupby('Type')['Rating'].mean())

# display top 5 apps having maximum installs
print(df['Installs'])
# index=df['Installs'].sort_values(ascending=False).max().index
# print(df.iloc[index])
print(df['Installs'].dtype)
df['Installs_1']=df['Installs'].str.replace(',','')
print(df.head())
df['Installs_1']=df['Installs_1'].str.replace('+','')
print(df.head())
# print(df['Installs_1'].astype('int'))
print(df[df['Installs_1']=='Free'])
df['Installs_1']=df['Installs_1'].str.replace('Free','0')
df['Installs_1']=df['Installs_1'].astype('int')
print(df['Installs'].dtype)
index=df['Installs_1'].sort_values(ascending=False).head().index
print(df.iloc[index]['App'])

