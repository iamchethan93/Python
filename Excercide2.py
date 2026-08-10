# ## Write a code to translate message into secret code.
# Rules 
# #Coding
# 1) If the length is less than 3 reverse the code.
# 2) If length is > 3 remove 1st letter and append it at the end of the code and add random three letters at the statrting and ending.


# #Decoding
# If the length is less than 3 reverse the code else remove the 3 characters at the start and end of the code and take the last character and add to the start.

# Eg : Chethan
# Coding
# remove 1st charcter and add it at the end.
# hethanc
# add random 3 characters at the start and end 
# sghhethanCtyu

# Decoding
# remove  3 characters from start and End 
# hethanC
# Add back the last character to front 
# Chethan


# Code logic 

# check if length is > 3
# if yes reverse and print the code.
# if no identify the last character(-1) and append it to the last index.

#Code
def encrypt(str):
    if len(str)>3:
        #Moving the first char to last
        fChar=str[0]
        str="cgy" + str[1:] + fChar + "nji"
        #print(f" Encrypted value is: {str}")
        return str
    else:
        #print(f"Encrypted value is {str[::-1]}")
        return str[::-1]

def decrypt(str):
    if len(str)>3:
        str = str[3:-3]
        lChar = str[-1]
        str = lChar + str[:-1]
        #print(f"Decrypted code is {str}")
        return str
    else:
        #print(f"Decrypted value is {str[::-1]}")
        return str[::-1]

#Ask for input
x = input("Do you want to encrypt or decrypt a message : ")
if x.lower()=="encrypt" or x.lower()=="decrypt":
    strng = input("Enter the value: ")
    if x.lower()=='encrypt':
        print(f"Encrypted value : {encrypt(strng)}")
    else:
        print(f"Decrypted value : {decrypt(strng)}")
else:
    print("Please select either Encrypt or decrypt. No other input is supported")

