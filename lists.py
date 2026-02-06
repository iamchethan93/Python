l = [3,4,5,"Chethan",True]
print(type(l))

#lists are ordered collection of items

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])


#slicing
# l[starting index : ending index : items to jump]

print (l[0:4:2])  


#List comphrehension - Generates a list on the fly
lst = [i*i for i in range(4)]
print(lst)

lst1 = [i*i for i in range(4) if i%2 ==0]
print(lst1)

#List methods.
l = [11,3,2,21,1]
l.append(13)

print(l)
l.sort()
print(l)

# m = l
# m[0]=0
# print(l)

#Never change values based on list

m = l.copy() #orignal values of L are retained and not changed.
m[0]=0
print(l)
print(m)

m = [999,1000,1001]
l.extend(m)
print(l)

a = [1,2,4]
b = [4,5,6]
print(a + b) 



