class employee1():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class childEmployee(employee1):
    def __init__(self, name, age, salary, id):
        self.name = name
        self.age = age
        self.salary = salary 
        self.id = id 

emp1 = employee1("Jethalaal",45,25000)
print(emp1.name)
print(emp1.age)
print(emp1.salary) 

emp2 = childEmployee("babita",27,56000,2)
print(emp2.id, emp2.name, emp2.age, emp2.salary )