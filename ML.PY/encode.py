# encoding :-
import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder

#Label Encoder :-
data={'name':['shubham','ashish','ajay','vijay'],
      'age':[25,32,34,35],
      'city':['kolhapur','pune','kolhapur','mumbai']}
df=pd.DataFrame(data)
print(df)
l=LabelEncoder()
df['city']=l.fit_transform(df['city'])
print(df)

# One Hot Encoding :-
df=pd.get_dummies(df,columns=['city'])
print(df)