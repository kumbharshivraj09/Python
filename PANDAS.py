import pandas


data=pandas.read_csv('myFile.csv')
'''print(data)  # print csv file

print(data.sallary) #print only sallary column
print(data.sallary.min()) #print minimum sallary
print(data.sallary.max()) #print maximum sallary
print(data.sallary.sum()) #print total sallary
print(data[data.id==107]) #find the employees
print(data[data.sallary==data.sallary.max()])
print(data.sallary.mean()) # prinnt average sallary

eid=data[data.id==105] #print emp first name and last name
print(eid.firstname.values[0],eid.lastname.values[0])


sallary=data.sallary.to_list()
for sal in sallary:
    print(sal)'''

#change the sallary of gale to 50000

data.loc[data.id==105,'sallary']=50000
print(data)

#remove data of vins

data=data.drop(7)
print(data)

#add the data with sallary to minimum to maximnum : 
data=data.sort_values(by='sallary')
print(data)

#add new column bonus with 10% discount sallary

data['bonus']=data.sallary*0.1
print(data)


data.to_csv('myfile_modified')