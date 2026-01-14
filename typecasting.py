#Conversion of one datatype to another dataype is called typecasting
a = "1"
b = "2"
print(a+b)

a = int(a)
b = int(b)
print(a+b)

#implicit typecasting
x = 5       # int
y = 2.3     # float 
z = x + y   # implicit typecasting of int to float
print(z)    # Output: 7.3
print(type(z))  # Output: <class 'float'>


# If y was converted to int there would be data loss. 
# Python automatically converts int to float to prevent this data loss.
# Conversion is based on hierarchy.
# int -> float -> complex.