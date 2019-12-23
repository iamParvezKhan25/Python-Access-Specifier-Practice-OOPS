class Company:
    def __init__(self, name, proj, ccode):
        self.name = name
        self._proj  = proj
        self.ccode = ccode
 
    def show(self):
        print("the code of company", self.ccode) 

class Emp(Company):
    def __init__(self, eName, eSal, cName, cProj, ccode):
        Company.__init__(self, cName, cProj, ccode)
        self.name = eName
        self.__sal = eSal 

    def showSalary(self):
        print("Salary of " , self.name , "is" , self.__sal)

c = Company("Pathan Industry","Mark 25",'MPK-15')

e  = Emp("Dev babu",25000,c.name,c._proj,c.ccode)

print("Welcome to ", c.name)
print("Here ", e.name, "is wokrking on ",e._proj)

e.showSalary()

print(" ")
print(" ")
print(" ")

print("\t Declared variable : \n")
print("Company Class :::\n")
print(c.name)
print(c._proj)

print(c.ccode)

print("\t Declared variable : \n")
print("Company Class :::\n")
print(e.name)
print(e._Emp__sal)