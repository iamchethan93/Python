# Constructor is used to initialise and create an object of a class. 
# It gets called automatically when an object of class is created. It always returns none.
# Two types of Constructors Parameterised(which accepts arguments) and plain/default (no arguments).

class Person:
    def __init__(self):
        print("Hello")

    def info(self,name,age):
        print(f"{name} {age}")

a = Person()
a.info("cbc",45)


# Function : Peice of code that does a specific function.
# Method : Function inside a class.
# Object : Instance of a class.
# Object_arguments : Params you pass while creating an instance of a class.
# Constructor arguments are passed when creating the object.
# Method arguments are passed when calling the method.
