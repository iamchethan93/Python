class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print(f"He codes in Python")

e1 = Employee("cbc",1186)
e1.showDetails()

e2 = Programmer("cbc",1186)
e2.showLanguage()