import oop

n=  input("enter a name : ") 
a=int(input("enter  age : ")) 
emp1=oop.Employees(n,a)
n=  input("enter a name : ") 
a=int(input("enter  age : ")) 
emp3=oop.Employees(n,a)
n=  input("enter a name : ") 
a=int(input("enter  age : ")) 
emp2=oop.Employees(n,a)


emp1.emp_info()
emp2.emp_info()
emp3.emp_info()
