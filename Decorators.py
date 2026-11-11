# # Decorator is a function that accepts a function as input, modifies the behaviour of the function and returns a function.
# # def greet():
# #     print("Hello")



# # Now imagine you want to print a message before and after greet() executes.

# def my_dec(func):
#     def wrapper():
#         print("Before Execution")
#         func()
#         print("After Execution")
#     return wrapper

# # decorated_greet = my_dec(greet)
# # decorated_greet()

# @my_dec
# def greet():
#     print("Hello")

# greet()


# lets use arguments


def my_dec(func):
    def wrapper(*args, **kwargs):
        print("Before Execution")
        result = func(*args, **kwargs)
        print("After Execution")
        return result
    return wrapper



@my_dec
def greet(n):
    print(f"Hello {n}")

greet("CBC")


