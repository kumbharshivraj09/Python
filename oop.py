#OBJECT ORIENTED PROGRAMMING : 

#class : a class is a blueprint or a template for creating object and 
# defines the structure and behaviour of that object


class Employees:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def emp_info(self):
        print(f'name is {self.name} and age is {self.age}')    

    # def name_change(self,new_name):
    #     self.name=new_name 
    #     print(f'name changed to {new_name}')   

n=  input("enter a name : ") 
a=int(input("enter  age : ")) 
emp1=Employees(n,a)
n=  input("enter a name : ") 
a=int(input("enter  age : ")) 
emp3=Employees(n,a)
n=  input("enter a name : ") 
a=int(input("enter  age : ")) 
emp2=Employees(n,a)

# print(emp1.age)
# print(emp1.name)
# print(emp2.name)
# print(emp3.name)
# print(emp2.age)
# print(emp3.age)

emp1.emp_info()
emp2.emp_info()
emp3.emp_info()




# object :
# an object is an instance of a class . with its own unique data ability to perform actions.

'''

-name                                     
     -------->class- employees------>object : - emp1
-age                                            - emp2
  |                                            - emp3
  employee info                                  
                                                    

'''


