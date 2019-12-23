class Base1():
    def __init__(self):
        self.str1 = "Khan 1"
        print("Base 1")

class Base2():
    def __init__(self):
        self.str2 = "Khan 2"
        print ("Base 2")

class Derived(Base1, Base2):
    def __init__(self):

        # calling Construction of 'Base 1' & 'Base 2'
        Base1.__init__(self)
        Base2.__init__(self)

        print("Derived")

    def printStr(self):
        print(self.str1, self.str2)

obj = Derived()

obj.printStr()