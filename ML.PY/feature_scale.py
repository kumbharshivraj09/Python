import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler

# TYPES OF FEATURE SCALING:
# STANDARDIZATION:-
df={
    'Age':[25,20,30,35],
    'Sallary':[25000,40000,35000,65000]
}
data=pd.DataFrame(df)
print(data)
x=data[['Age','Sallary']]
scale=StandardScaler()
xScale=scale.fit_transform(x)
# print(xScale)

# NORMALIZATION :-(MIN MAX SCALE)

from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler()
sc=scal.fit_transform(x)
# print(sc)
