import pandas as pd
df=pd.read_csv('myFile.csv')
print(df)

#first 3 rows
print(df.head(3))

#last 3 rows 
print(df.tail(3))

#check datatype of each column
print(df.dtypes)

#null 
print(df.isnull())

# total number of rows and columns in dataset :
print(df.info())
print(len(df))
print(len(df.columns))

#maximum sallary
print(df['sallary'].max())

# minimum sallary
print(df['sallary'].min())

# average sallary 
print(df['sallary'].mean())

firstname=df[df['firstname']=='Gale']
print(firstname)

# find the email following id 

print(df[df['id']==104]['email'])