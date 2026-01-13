#PYTHON BUILT IN MODULE
# FOR EXAMPLLE : 1 - RANDOM
#                2 - DATETIME


import random
from datetime import datetime

# print(random.random())
# print(random.randint(1,11))

# list=['apple','mango','banana','kiwi','orange']
# print(random.choice(list))

# print(random.uniform(4.6,4.9))

# while True:
#     print(f'number is : {random.randint(1,6)}')
#     user_input=input("do you wand to continue ? y/n : ")
#     if user_input=='n':
#         break


cur_date=datetime.now()
print(cur_date)
print(cur_date.time())
print(cur_date.day)
print(cur_date.strftime('%y-%m-%d %HH-%mm'))