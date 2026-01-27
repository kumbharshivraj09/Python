import pandas as pd
import numpy as np
df=pd.read_csv('Salaries.csv')
print(df)

print(df.head())#display first five rows 
print(df.tail())#display last five rows 
print(df.columns)#display columns
print(df.isnull())#display null values
print(df.info())#display information
print(df.describe(include='all'))#statistics for all columns

# drop id,notes agency columns
print(df.columns)
print(df.drop(['Id','Notes',"Agency"],axis=1))
print(df.head(1))

# find occurence of the employee name (top 5)
print(df["EmployeeName"].value_counts().head(5))

# find the number of unique job titles 
print(df["JobTitle"].unique())

# total number of job titles contain captain
print(len(df[df['JobTitle'].str.contains('Captain')]))

# display all employyes names from the fire department
print(df[df['JobTitle'].str.contains('fire',case=False)]['EmployeeName'])

# find min,max,avg on basepay
print(df['BasePay'].describe())
print(df['BasePay'])

# replace 'not provide' in employee name column to nan

df['EmployeeName']=df['EmployeeName'].replace('Not provided',np.nan)
print(df['EmployeeName'])

# drop the rows having 5 missing values
print(df.drop(df[df.isnull().sum(axis=1)==5].index
              ,axis=0,inplace=True))
print(df.isnull().sum(axis=1))


# find the job title of albert pardini
print(df.columns)
print(df[df['EmployeeName']=='ALBERT PARDINI']['JobTitle'])

# how much abert pardini make(include benifits)?
print(df[df['EmployeeName']=='ALBERT PARDINI']['TotalPayBenefits'])

# find the most 5 common job
print(df['JobTitle'].value_counts().head())
