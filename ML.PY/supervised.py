# SUPERVISED MACHINE LEARNING :-
import pandas as pd 
from sklearn.linear_model import LinearRegression
# 1.LinearRegration :-
df={
    'S_H':[1,2,3,4,5],
    'M':[40,45,55,65,35]
}
data=pd.DataFrame(df)
model=LinearRegression()
x=data[['S_H']]
y=data['M']
model.fit(x,y)
# H=float(input('Enter How Many Hours You Studies : '))
# prediction=model.predict([[H]])
# print(prediction)

# classification :-
# 1.Logistic Regration :-
from sklearn.linear_model import LogisticRegression
df={
    'M':[30,39,55,65,35],
    'R':[0,0,1,1,1]
}
data=pd.DataFrame(df)
model=LogisticRegression()
x=data[['M']]
y=data['R']
model.fit(x,y)
# M=float(input('Enter Your Marks : '))
# prediction=model.predict([[M]])
# if prediction==1:
#     print(f'Based On Marks {M},You Are Pass ')
# else:
#     print(f'Based On Marks {M},You Are Fail ')

#KNN :-
from sklearn.neighbors import KNeighborsClassifier
# df={
#     "fruit_W_S":[180,200,250,30,330,380],
#     'S':[7,7.5,8,8.5,9,9.5],
#     'F':[0,0,0,1,1,1]
# } 
# data=pd.DataFrame(df)
# x=data[['fruit_W_S','S']]
# y=data['F']
# model=KNeighborsClassifier()
# model.fit(x,y)
# Weight=float(input("Enter a Weight in Kg :"))
# size=float(input("Enter a Size in Cm :"))
# prediction=model.predict([[Weight,size]])[0]
# if prediction==0:
#     print("THis Is Likely Apple ")
# else:
    # print("This is likely Orange ")

# Decison Tree :-
from sklearn.tree import DecisionTreeClassifier
data={
    'size':[7,8,6,9,10],
    'Shade':[1,2,0.8,4,5],
    'R':[0,0,0,1,1]
}
data=pd.DataFrame(data)

x=data[['size','Shade']]
y=data['R']
model=DecisionTreeClassifier()

model.fit(x,y)

S=float(input("Enter a Size in CM : "))
s=float(input("enter a shade in number : "))
result=model.predict([[S,s]])
if result==0:
    print("this is likely apple : ")
else:
    print('this is likely orange ')
