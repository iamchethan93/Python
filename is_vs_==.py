# is comapres exact location of object in memory. 
# == compares the values of the objects.


a = 4
b = '4'

print(a is b) # exact location
print(a==b) # exact value
print("==============")

a = [1,2,3,4]
b = [1,2,3,4]
print(a is b)
print(a==b) 

print("==============")
a = 3
b = 3
print(a is b)
print(a==b) 
#- Here both comes out as true because when Python creates a constant/immutable object, it will leverage the same memory location for another 
#. constant with same value. Meaning both a and b value being same (3) they will reside in the same location.



