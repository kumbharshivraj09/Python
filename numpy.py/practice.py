import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#data structure (restaurent id,2021,2022,2023,2024)
sales_data=np.array([
    [1,150000,180000,220000,250000],#Biryani
    [2,120000,140000,160000,190000],#pizza
    [3,200000,230000,260000,300000],#burger
    [4,180000,210000,240000,270000],#chai
    [5,160000,185000,205000,230000]#wadapav

])

print(sales_data)

# find the shape
print(np.shape(sales_data))

# first 3 restaurent
print(sales_data[:3])
print(sales_data[:,1:])

# total sales per year
sales_per_year=sales_data.sum(axis=0)
print("total sales per year : ",sales_per_year)

# minimum sales per rest
print(np.min(sales_data[:,1:],axis=1))

# maximnum sales per year
print(np.max(sales_data[:,1:],axis=0))

# avg sales per rest
print(np.mean(sales_data[:,1:],axis=1))

# cumilatvie sum 
cumsum=np.cumsum(sales_data[:,1:],axis=1)
print(cumsum)

# # matplotlib 
# plt.figure(figsize=(10,6))
# plt.plot(np.mean(cumsum,axis=0))
# plt.title("avg cumilative sales")
# plt.xlabel("years")
# plt.ylabel("sales")
# plt.grid(True)
# plt.show()

# df=pd.DataFrame(sales_data)
# print(df.describe(include='all'))
# print(np.median(sales_data))

vector1=np.array([1,2,3,4,5])
vector2=np.array([6,7,8,9,0])
print(vector1+vector2)

restaurent_type=np.array(["biryani","pizza","burger","chai","wadapav"])
vectorized_upper=np.vectorize(str.upper)
print(vectorized_upper(restaurent_type))

monthly_avg=sales_data[:,1:]/12
print(monthly_avg)