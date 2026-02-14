import pandas as pd 
# import numpy as np 
# import matplotlib.pyplot as plt 
# import seaborn as sns 

# df=pd.read_csv('Customer Churn.csv')
# print(df.head())

# print(df.info())

# print(df.describe())

# print(df.shape)

# print(df.isnull().sum())

# print(df.columns)

# print(df.dtypes)

# print(df['TotalCharges'].isin(['']).sum())

# df['TotalCharges']=df['TotalCharges'].replace(' ','0')
# df['TotalCharges']=df['TotalCharges'].astype('float')
# print(df.dtypes)
# print(df['TotalCharges'].isin(['0']).value_counts())

# # check duplicate : 
# print(df.duplicated().sum())

# # converted 0 and 1 value of senior citzon to yes/no to make easy to understand

# # def convert(value):
# #     if value==1:
# #         return 'Yes'
# #     else:
# #         return 'No'

# # df['SeniorCitizen']=df['SeniorCitizen'].apply(convert)
# # print(df['SeniorCitizen'].value_counts())

# # # ax=sns.countplot(x='SeniorCitizen',data=df)
# # # ax.bar_label(ax.containers[0])
# # # plt.show()

# # # create countplot on Churn
# # print(df['Churn'])
# # ax=sns.countplot(x='Churn',data=df,hue='gender')
# # for container in ax.containers:
# #     ax.bar_label(container)
# # plt.show()

# # # create pie chart on churn 
# # gb=df.groupby('Churn').agg({"Churn":"count"})
# # print(gb)

# # plt.pie(gb['Churn'],labels=gb.index,autopct='%1.2f%%')
# # plt.title("PERCENTAGE OF CHURN CUSTOMERS")
# # plt.show()

# # bx=sns.countplot(x='gender',data=df,hue='SeniorCitizen',)
# # for container in bx.containers:
# #     bx.bar_label(container)
# # plt.title("GENDER")
# # plt.xlabel('male female')
# # plt.ylabel('value')    
# # plt.show()    

# # create histogram : 
# sns.histplot(x='tenure',data=df,bins=70,hue='Churn')
# plt.show()

# bx=sns.countplot(x="Contract",data=df,hue='Churn')
# for container in bx.containers:
#     bx.bar_label(container)

# plt.show()

dattt=pd.read_sql_query('first.sql')
print(dattt)






