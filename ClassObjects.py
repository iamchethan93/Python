# # Class is a blue-print and object is an instance(created from) of that blue print.
# # Self is a keyword that represents the paticular instance of a class


# class Person :
#     name = "Chethan"
#     age = "33"
#     Networth = "1000Cr"

#     def info(self):
#         print(f"{self.name} is of age {self.age} and is worth {self.Networth}")

#     def info1(name,age,Networth):
#         print(f"{name} is of age {age} and is worth {Networth}")


# a = Person()
# a.info()

# a.name = "Sona"
# a.age = 4
# a.Networth = "25cr"
# a.info()


# b=Person()
# b.name = "Bindu"
# b.age = 30
# b.Networth = "250cr"
# b.info()



# Build a BankAccount class.
# Your class should:
# 1. Accept an account holder's name and initial balance when creating an object.
# 2. Have a deposit() method that adds money to the balance.
# 3. Have a withdraw() method that deducts money from the balance.
# 4. Have a display_balance() method that prints the account holder's name and current balance.
# 5. Create two different bank account objects and perform transactions on them.
# Expected behavior: Depositing money into one account should not change the other account's balance.


class BankAccount:
    def __init__(self,name,initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount to deposit")

    def withdraw (self,amount):
        if amount <= 0 :
            print("Not valid amount")
        elif amount > self.balance :
            print("Not enough balance")
        else :
            self.balance -= amount


    def display_balance(self):
            print(f"Name of the accontant is {self.name}, balance is {self.balance}")

a = BankAccount("Chethan", 1000)
a.deposit(0)
a.display_balance()

b = BankAccount("B", 1000)
b.withdraw(1500)
b.display_balance()

