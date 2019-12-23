class Base():
    def __init__(self, name):
        self.__name = name 
    
    def getName(self):
        return self.__name

class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self._age = age 

    def getAge(self):
        return self._age

class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address

GCobj = GrandChild("Parvez Khan",24,"Ahmedabad")
print(GCobj.getName())
print(GCobj.getAge())
print(GCobj.getAddress())

Bobj = Base("Shivani")
print(Bobj._Base__name)