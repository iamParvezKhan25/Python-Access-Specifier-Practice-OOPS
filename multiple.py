#Parent Class 1
class employee1():
    def __init__(self, name, age, salary):
        self.name = name 
        self.age = age 
        self.salary = salary 

# Parent Class 2 (Also Parent Class) 
class employee2():
    def __init__(self, name, age, salary, id):
        self.name = name 
        self.age = age 
        self.salary  = salary 
        self.id = id 

class childEmp(employee1, employee2):
    def __init__(self, name, age, salary, id):
        self.name = name 
        self.age = age 
        self.salary = salary
        self.id = id 

objEmp1 = employee1("Salman",47,47000)
objEmp2 = employee2("Aamir",57,27000,25)

print(objEmp1.name, '-', objEmp1.age, '-', objEmp1.salary)
print(objEmp2.id,'-',objEmp2.name, '-', objEmp2.age, '-', objEmp2.salary)