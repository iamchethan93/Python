#Main use is to handle error. When imp lines of code have to be executed and not missed due to erroring of other block we use try and except.


# a = int(input("Enter the number: "))2
# print(f"Table of {a} is :")
# for i in range(1,11):
#     print(f"{a} X {i} = {a*i}")

# print("Some imp lines of code")


#Now if we provide any string as ip then the code errors out without executing the imp lines of code.
#Hence to catch these errors we use try except blocks and not to disrupt the normal execution of a program.



# a = input("Enter the number: ")
# print(f"Table of {a} is :")
# b=[1,2]
# try:
#     for i in range(1,11):
#         print(f"{a} X {i} = {int(a)*i}")
#     print(b[int(a)])
# except ValueError:
#     print("Invalid Input")

# except IndexError:
#     print("Index error")

# print("Some imp lines of code")

#Finally keyword. #Used in the try except to execute code that needs to be executed ireespective of the erros
def cbc():
    try:
        l=[1,2,3,4,5,6]
        i = input("Enter the index:")
        print(l[int(i)])
        return 0
    except:
        print("Some error occured")
        return 1
    finally:
        print("Imp lines of code")

x=cbc()
print(x)




