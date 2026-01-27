import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("adult.csv")
print(df)

print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)

'''['age', 'workclass', 'fnlwgt', 'education', 'educational-num',
       'marital-status', 'occupation', 'relationship', 'race', 'gender',      
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',    
       'income'],
      dtype='object'''

# fetch randomm sampple from the dataset (50%)
print(df.sample(frac=0.50,random_state=11))

# check null values inthe dataset 
print(df.isnull().sum())

# perform dat cleaning [replace '?' with nan]

# print(df.isin(['?']).replace('?',np.nan))
df['workclass']=df['workclass'].replace('?',np.nan)
df['occupation']=df['occupation'].replace('?',np.nan)
df['native-country']=df['native-country'].replace('?',np.nan)
print(df.isin(['?']).sum())
print(df.isnull().sum())

# drop missing values 
missing_per=df.isnull().sum()*100/len(df)
print(missing_per)
print(df.dropna(how='any',inplace=True))
missing_per=df.isnull().sum()*100/len(df)
print(missing_per)

# check for duplicate data and drop them
print(df.duplicated().any())
print(df.drop_duplicates())
print(df.shape)

# # Drop the column education-num,capital-gain and capital-loss
# print(df.columns)
# print(df['education'].unique())
# dat=df.drop(['education-num','capital-gain', 'capital-loss'],axis=1)
# print(dat)
# print(df.columns)

# univariate analysis
# what is the distribution of age column
print(df['age'].describe())
print(df['age'].hist())

# find the number of personn having age between  17 to 48
# using between method

print(sum((df['age']>17)& (df['age']<48)))

print(df[df['age'].between(17,48)])

# what is the distribution of workclass column
print(df['workclass'].describe())
print(plt.figure(figsize=(10,10)))
print(df['workclass'].hist())

# how many person aving bachelor or master degree
p1=df['education']=='Bachlors'
p2=df['education']=='Masters'
print(len(p1))
print(len(p2))

print(sum(df['education'].isin(['Bachelors',"Masters"])))

# Bivariate analysis
print(sns.boxplot(x='income',y='age',data=df))
# replace income values ["<=50k,'>50k"] with 0 and 1
print(df['income'].unique())
print(df['income'].value_counts())

# df.replace(to_replace=['<=50k','>50k'],value=[0,1],inplace=True)
# def income_data(inco):
#     if inco=='<=50k':
#         return 0
#     else:
#         return 1
# df['income'].apply(income_data)
# df['encoded income']=df['income'].apply(income_data)   
# print(df.head(1))



# which  workclasss getting the highest salary
# print(df.groupby('workclass')['income'].mean())
print(df.head(2))