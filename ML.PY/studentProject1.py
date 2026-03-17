import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
df={
    "Hours":[1,2,3,4,5,6],
    'Mark':[52,57,65,70,75,80]
}
data=pd.DataFrame(df)
print(data)

model=LinearRegression()
x=data[['Hours']]
y=data['Mark']
model.fit(x,y)
prediction=model.predict(x)

print(prediction)
print('MAE : ',mean_absolute_error(y,prediction))
print('MSE : ',mean_squared_error(y,prediction))
print('RMSE : ',np.sqrt(mean_absolute_error(y,prediction)))
new_predictionn=model.predict([[7]])
print(new_predictionn)