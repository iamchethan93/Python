#Tuple cannot be changed once defined.

a = (1,2,3,4,5,"green",True)
print(type(a))

a[0] = 1 # Gives error

#When sliced it returns a new tuple

x= a[0:3]
print(type(x))

tup = (1,2,3,44,44,44,44,5,6,7)
print(tup.count(44))




