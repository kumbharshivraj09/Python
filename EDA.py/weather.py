import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

#WEATHER DATA :-

df=pd.read_csv('1. Weather Data.csv')
# print(df.head())
# print(df.shape)
# print(df.dtypes)
# print(df.columns)
# print(df.isnull().sum())
# print(df.info())
# print(df.describe())

#find the all unique "wind speed "values in the data 
print(df.columns)
# print(df['Wind Speed_km/h'].nunique())
# print(df['Wind Speed_km/h'].unique())

# #find the number of times when  the "wheather isexactly clear "
# print(df['Weather'].value_counts())#1st way
# print(df[df['Weather']=='Clear'])#2nd filtering
# print(df.groupby('Weather').get_group("Clear"))#3 

#find the number of times when the "wind speed exactly 4k/m"
print(df['Wind Speed_km/h'].nunique())
print(df['Wind Speed_km/h'].value_counts())
print(df[df['Wind Speed_km/h']==4])

#find out all null value in data 
print(df.isna().sum())

#rename the column weather of the datframe to weather condition
print(df.rename(columns={'Weather':'Weather Condition'}))
print(df.head(2))

#what is the mean visability:-
print(df['Visibility_km'].mean())

#what is the std of presure in this data
print(df['Press_kPa'].std())

#what is the variancce of relative humidity in this data
print(df['Rel Hum_%'].var())

#find all instances when snow was recorded
print(df[df['Weather']=='Snow'])
print(df['Weather'].value_counts())
print(df[df['Weather'].str.contains('Snow')])

#find all instances when wind speed is above 24 and visibility is 25
print(df[(df['Visibility_km']==25) & (df['Wind Speed_km/h']>24)])

#what is the mean value of each column aginst each weather condition
print(df['Weather'].dtype)
# df['Weather']=pd.to_numeric(df['Weather'],errors='coerce')
# print(df['Weather'].dtype)

print(df.groupby("Weather").mean(numeric_only=True))

#what is the mi & max value of each column against each weather
print(df.groupby("Weather").min(numeric_only=True))
print(df.groupby("Weather").max(numeric_only=True))

#show all records where condition is fog 
print(df.groupby('Weather').get_group('Fog'))

#find the innstance when weather is clear or visibility above 40
print(df[(df['Weather']=='Clear')|(df['Visibility_km']>40)])


print(df[((df['Weather']=='Clear')&(df['Rel Hum_%']>50))|(df['Visibility_km']>40)])