import pandas as pd 
import numpy as np 

# REGRATION MATRICS :-
# 1.MAE-mean absolute error 
# 2.MSE-mean squred error
# 3.RMSE-root mean squred error
'''

    "student":['A','B','C','D'],
    "Actual_M":[80,90,60,100],
    "Mdel_P":[75,80,70,95],
    "Mist":[5,10,10,5]
MAE:-
RULES -
TAKE THE MISTAKE DIFFERENCE
REMVE THE MINUS SIGN
ADD
DIVIDE
out:- 30/4=7.5

MSE:-
MISTAKE SQURE THEM
ADD
DIVIDE TOTAL
out:- 62.5

RMSE:
ROOT MEAN  SQURED ERROR

'''
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error
Actual_M=[80,90,60,100]
Mdel_P=[75,80,70,95]

print("MAE : ",mean_absolute_error(Actual_M,Mdel_P))
print("MSE : ",mean_squared_error(Actual_M,Mdel_P))
print("RMSE : ",root_mean_squared_error(Actual_M,Mdel_P))
print("RMSE : ",np.sqrt(mean_squared_error(Actual_M,Mdel_P)))
