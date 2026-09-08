# #Enumerate - A fucntion that is used to return both index and value of the list of elements. Ideally we will need to specify index separately. Eg below


# marks = [19, 25, 67, 87, 45, 100]
# index = 0
# for i in marks:
#     print(i)
#     if index == 3: print("Good Job")
#     index +=1

# #We need to declare index and compute the value as well. Enumerate solves this problem.
# #enumerate() lets you loop through a sequence while getting both the index and the value.

# marks = [19, 25, 67, 87, 45, 100]
# index = 0
# for index,i in enumerate(marks):
#     print(i)
#     if index == 3: print("Good Job")

# #We can custom declare the start value of the index as well

# marks = [19, 25, 67, 87, 45, 100]
# index = 0
# for index,i in enumerate(marks,start=1):
#     print(i)
#     if index == 3: print("Good Job")


#Challenges

names = ["Rahul", "Amit", "Priya", "Neha"]
for index,name in enumerate(names):
    print(index,name)



names = ["Rahul", "Amit", "Priya", "Neha"]
for index,name in enumerate(names,start=1):
    print(index,name)

#Use enumerate to find position of  
for index,name in enumerate(names):
    if name == 'Priya': print(f"Priya is at position {index}")

#Print only the marks greater than 60 along with their index.
marks = [45, 78, 32, 91, 56, 88]
for index,mark in enumerate(marks):
    if mark >60:
        print(index,mark)

#Use enumerate() to print:
# John scored 75
# Alice scored 92
# Bob scored 68
# David scored 85
names = ["John", "Alice", "Bob", "David"]
marks = [75, 92, 68, 85]


for index,(n,m) in enumerate(zip(names,marks)):
    print(f"{n} scored {m}")

#Hint: You only need enumerate() on one of the lists.

for index,n in enumerate(names):
    print(f"{n} scored {marks[index]}")