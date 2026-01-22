import pandas as pd 

data={

    'name':['archana','sanket','vishal','shrisha','omkar','mitali','shubham','sanika'],
    "mark":[58,98,68,85,87,99,97,89],
    "gender":['female','male','male','female','male','female','male','female']
}

df=pd.DataFrame(data)
print(df)

#Display first 5 row : 
print(df.head(5))

#Display last 5 row : 
print(df.tail(5))

#find shape our dataset
print(df.shape)
print("number of rows",df.shape[0])
print("number of columns",df.shape[1])

#get information about dataset
print(df.info())

#check null values : 

print(df.isnull())
print(df.isnull().sum())

# get overall statistic about our dataset : 
print(df.describe(include="all"))
print(df.describe())

#find unique value in gender columns :
print(df["gender"].unique()) 

#find the number of unique values in gender 
print(df["gender"].nunique())

# display count of unique values in gender columns
print(df['gender'].value_counts())

# find the total number of student having marks between 90 to 100
# using between method

print(df[(df['mark']>90) & (df['mark']<100)])
# between method : 
print(df.loc[df['mark'].between(90,100),['name','mark']])

# find avarage mark : 
print(df['mark'].mean())

#aplay method : 
def marks(x):
    return x/2
df['halfmark']=df['mark'].apply(marks)
print(df)

#lenth of string in name column
print(df['name'].apply(len))

#map fuunction : 
print(df['gender'].map({'male':1,'female':0}))
df['male_female']=df['gender'].map({'male':1,'female':0})
print(df)

# drop columns 
print(df.drop('male_female',axis=1))
print(df.drop('halfmark',axis=1))

#print name of the columns : 
print(df.columns)

#sort the data frame as per the mark columns 

print(df.sort_values('mark',ascending=True))

# display name and mark of the female student only : 
df['gender']=='female'
print(df[df['gender']=='female'][['name','mark']])


