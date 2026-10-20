# f = open('cbc.txt','r')
# #File name and open mode like read(r), write(w) and append(a)
# print(f.read())
#f.close()

#r mode is default. Even if not mentioned it reads.
#In write mode even if the file does not excist it will create a file.


#Writing to a file

# f = open('cbc.txt1','w')
# f.write("Trust in god")

# f = open('cbc.txt1','a')
# f.write("Trust in god\n")
# f.close()

#Use with mode closeing is not needed.

# with open('cbc.txt') as f:
#     print(f.readline())
#     print(f.readline())

with open('cbc.txt') as file:
    print(file.read(6))
    file.seek(0)
    print(file.read(4))
    file.seek(0)
    print(file.readlines(1))
    print(file.tell())

