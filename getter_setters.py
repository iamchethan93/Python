# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance

# account = BankAccount(1000)
# account = BankAccount(-1000)
# print(account.balance)


# - Here we were able to update the balance to negative which in ideal case should not be possible.
# - What is a getter?
# - A getter is a method used to retrieve an object's attribute.


class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,amount):
        if amount > 0:
            self._balance = amount
        else :
            print(f"Invalid amount")

a= BankAccount(1000)
print(a.balance)

a.balance = 2000
print(a.balance)


