fruit = 'apple'
print(len(fruit))

#Print all characters using index
print(fruit[0:]) # starts from 0 till last

#Print from second charcter to last 
print(fruit[1:])

#Print from second charcter to 4th  
print(fruit[1:4])

#print last character 
print(fruit[-1])

#Negative slicing 

print(fruit[0:-1]) # Python adds len(fruit before -1 so the cmnd becomes print(fruit[0:len()fruit-1]))

print(fruit[-4:-3]) # Equal to print(fruit[len(fruit)-4:len(fruit)-3]) 

print(fruit[::-1])