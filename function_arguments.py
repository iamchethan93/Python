#Function arguments and return statement

#Default arguments
def average(a=1,b=2):
    print(f"The average is {(a+b)/2}")

average()

#It will assume default value until supplied otherwise.

average(5,1)

#Keyword Arguments
#You pass the keyword=value. So that the interpeter recognises the key and the value for that.

average(b=9, a=1)

#Requied arguments ---Argument that need to be passed.

#Multiple arguments 
def averages(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print(f"Average is {sum/(len(numbers))}")


averages(1,2,3,4)