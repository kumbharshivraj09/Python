import pandas as pd 
#read data from csv file into a data frame.

# df=pd.read_csv('myFile.csv')
# print(df)

data={
    "name":["rahul",'sagar','karan','ajay','omkar'],
    'age':[22,36,20,20,21],
    'city':['pune','nagpur','kolhapur','sangali','satara']
}

df=pd.DataFrame(data)
# print(df)

# df.to_csv('output.csv')
# df.to_excel('output.xlsx')
# df.to_json('output.json')
# df.to_html('output.html')

# df=pd.read_csv('myFile.csv')
# print("display 5 rows of first ")
# print(df.head(5))
# print(df.tail(5))

df=pd.read_csv('myFile.csv')
# print(" display info of data : ")
# print(df.info())

# describe method : 
df=pd.read_csv('myFile.csv')
print(df.describe())

