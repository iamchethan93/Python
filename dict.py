#Mapping of items in key value pairs. They are stored in ordered way.

info = {'name':'Karan', 'age':19, 'job':'unemployed'}
print(info)

print(info["name"])
# print(info["name1"])
print(info.get("name1")) ##Program will not error out when used .get

#keys
x ,y = info.keys(), info.values()
print(x,y)
print(type(x))
print(type(y))

for i in info.keys():
    print(f"Keys : {i}")

for i in info.values():
    print(f"Values : {i}")

print(info.items())


#Dictionary Methods
#update()
info.update({"Place":"Bangalore"})
print(info)

info.pop([-1])
print(info)


 