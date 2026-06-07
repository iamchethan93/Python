# Sets is a collection of well defined objects. Its unordered.
# Unique collection. As it is unordered we cannot access it using indexing

s = {1,2,3,4,3}
print(s)


#Create an empty set

cbc = {}
print(type(cbc)) #--> comes out as dict. 

#To create an empty set 
bc= set ()
print(type(bc))


#set methods

s = {1,4,2,6,4}
s1 = {7,8,9,4,2}
print(s.union(s1))

print(type(s))

s.update(s1)
print(s,s1)