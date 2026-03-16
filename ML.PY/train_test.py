import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data={
    'Study_Hr':[11,2,3,4,5],
    'Marks':[45,50,60,65,75]
}
df=pd.DataFrame(data)
x=df[['Study_Hr']]
y=df['Marks']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(y_train)
model=LinearRegression()
model.fit(x_train,y_train)
prediction=model.predict([[6]])
print(prediction)
print(x_test)
print(x_train)
print(y_test)
print(y_train)