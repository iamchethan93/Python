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

# info.pop()
# print(info)

# Test program
student = {
    "name" : "Chethan",
    "age" : "33",
    "city" : "Bangalore"
}

#print name and age
print(student['name'])
print(student["age"])

# add new key, value
student.update({"class":"top"})
print(student)

# Change the value
student.update({"class":"top1"})
print(student)

 #Print all keys using dict method

for i,j in student.items():
    print(i) 

 #Print all values using dict method

for i,j in student.items():
    print(j) 

#Print both kay and value

for i,j in student.items():
    print(i,"--->",j) 


# Given a string create a dict with count of frequency of each character.
word = "banana"

#iterate theought he word, if i in word +1 else 1


dic ={}
for i in word :
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

#Find students with highest marks

marks = {
    "John": 85,
    "Alice": 92,
    "Ak" : 85,
    "Bob": 78,
    "David": 88

} 
print(f"marks dict as list{list(marks.values())}")


#sort the dict based on values
#Values desc if same alphabetical

value_sorted_data = dict(sorted(marks.items(),key= lambda item : (-item[1],item[0])))
print(f"Values desc if same alphabetical : {value_sorted_data}")

#Values asc if same alphabetical
value_sorted_data = dict(sorted(marks.items(),key= lambda item : (item[1],item[0])))
print(f"Values asc if same alphabetical : {value_sorted_data}")


marks1 = {
    "John": 85,
    "Alice": 92,
    "Alice" : 85,
    "Bob": 78,
    "David": 88

} 
#Key asc if same asc of key values
key_sorted_data = dict(sorted(marks.items(),key= lambda item : (item[0],item[1])))
print(f"keys asc if same asc of key values : {key_sorted_data}")

#Key desc if same asc of key values
key_sorted_data = dict(sorted(marks.items(),key= lambda item : (item[0],item[1]),reverse=True))
print(f"keys desc if same asc of key values : {key_sorted_data}")

#Both key and values are strings.
strings = {
    "John": "A",
    "Alice": "B",
    "Alice" : "C",
    "Bob": "A",
    "David": "D"
} 
#Value asc if values are same keys asc
Value_sorted_data = dict(sorted(strings.items(),key= lambda item : (item[1],item[0])))
print(f"Value asc if values are same keys asc : {Value_sorted_data}")

#Value asc if values are same keys desc
Value_sorted_data = dict(sorted(strings.items(),key= lambda item : (item[1],-ord(item[0][1]))))
print(f"Value asc if values are same keys desc : {Value_sorted_data}")



data = {}
data[1] = "Integer One"
data[1.0] = "Float One"

print(type(data),data) 

if(1==1.0):
    print("yes")
else:
    print("No")




