# for loop : execute block of code repeatetly

'''for i in range(1,10):
    print('number')
    print(i)'''

#for loop for list
'''list = ["rohan","rohit","sham","sumit","sourabh","shubham","sujal","parth"]
for name in list:
    print(name)'''

#for loop for dictionary

'''subjects ={
'marathi':95,
'english':84,
'maths':97,
'hindi':89,
'science':82

}


for subject,mark in subjects.items():
    print(f'subject is : {subject} and mark is : {mark}')

for subject in subjects.keys():
    print(subject)'''

#num=int(input("enter number : "))
for num in range(1,101):
    if num%2==0:
        print(num)
