class employee():
    def __init__(self, name, age, salary):
        self.name = name 
        self.age = age
        self.salary = salary

class childEmp1(employee):
    def __init__(self, name, age, salary):
        self.name = name 
        self.age = age 
        self.salary = salary 

class childEmp2(childEmp1):
    def __init__(self, name, age, salary):
        self.name = name 
        self.age = age
        self.salary = salary

empObj1 = employee("Shah Rukh Khan", 47, 200000)
empObj2 = childEmp1("Salman Khan", 57,300000)  
empObj3 = childEmp2("Aamir Khan", 67, 400000)

print(empObj1.name)
print("-------")
print(empObj2.age)
print("-------")
print(empObj3.salary)