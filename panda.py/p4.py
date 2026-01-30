import pandas as pd 
import numpy  as np

df=pd.read_csv("train.csv")
print(df)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)

# data filtering
print(df.columns)
print(df[['Name', 'Sex', 'Age']])

print(df[df['Sex']=='male'])
print(sum(df['Sex']=='male'))

print(df[df['Survived']==1])
print(sum(df['Survived']==1))

# check null values
print(df.isnull().sum())

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.isnull())
per_missing=df.isnull().sum()*100/len(df)
print(per_missing)
print(df.drop('Cabin',axis=1,inplace=True))
print(df.isnull().sum())

# handling missing values

print(df['Embarked'])
print(df['Embarked'].mode())
print(df['Embarked'].fillna('S',inplace=True))
print(df.isnull().sum())

print(df['Age'].fillna(df['Age'].mean(),inplace=True))
print(df.isnull().sum())

# categorical data encoding
g=df['Sex'].map({'male':1,'female':0})
print(df.insert(5,'gender',g))
print(df.head())
print(df.columns) 

# sencond method
print(df['Embarked'].unique())
data=pd.get_dummies(df,columns=['Embarked'],drop_first=True)
print(data)
print(df.columns)

# what is univariate analysis
# how many people survived and how many died
print(df['Survived'].value_counts())
print(sns.countplot(df['Survived']))

# feature engineering

df['family_size']=df['SibSp']+df['Parch']
print(df.head())













