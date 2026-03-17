import pandas as pd
import numpy as np

# MODEL EVALUTION :-
# classificationn matrics:-
# 1.accuracy
# 2.pricision
# 3.recall
# 4.f1
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
# true answer what actulay happend
x_true=[1,0,1,0,1]
# model prediction 
y_predict=[0,1,1,1,0]

# evalution:-
# print("Accuracy :",accuracy_score(x_true,y_predict))
# print("precision :",precision_score(x_true,y_predict))
# print("Recall :",recall_score(x_true,y_predict))
# print("F1 :",f1_score(x_true,y_predict))

# confusion matrics:-
'''
tp:true-positive
tn:true-negative
fn:false-negative
fp:false-positive

'''
from sklearn.metrics import confusion_matrix
a_true=[1,0,0,1,1,1,0,1,0,0]
b_predict=[0,0,1,0,1,1,1,0,1,0]
print("Confusion Matrics :- ",confusion_matrix(a_true,b_predict))
# output:-[[2,3]
#          [3,2]]
"""
here output is 
[[tn,fp]
[fn,tp]]
"""
