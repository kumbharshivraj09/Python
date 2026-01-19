import pandas as pd 

#concatination : 
'''
vertically(row vise)
horizontally(columns vise)

'''

# vertically

df1=pd.DataFrame({
    "customer_name":['rohan','parth','rupesh'],
    'id':[1,2,3]
})
print(df1)
df2=pd.DataFrame({
    "customer_name":['yogesh','sanket','rahul'],
    'id':[4,5,6]
})

df3=pd.DataFrame({
    "customer_name":['ashish','vaibhav','sumit'],
    'id':[7,8,9]
})

df123=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(df123)