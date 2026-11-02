# Two players. Each have an option to put up snake/water/gun.
# Snake drinks water, water diffuses gun and Gun kills snake. 
# Use this rule to design the game and figure out who is the winner.
# P1_input = input("Enter P1's choice : ")
# P2_input = input("Enter P2's choice : ")

# if P1_input.upper() == 'SNAKE' and P2_input.upper() == 'WATER':
#     print(f"P1 is winner")
# elif P1_input.upper() == 'SNAKE' and P2_input.upper() == 'GUN':
#     print(f"P2 is winner")
# elif P1_input.upper() == 'WATER' and P2_input.upper() == 'SNAKE':
#      print(f"P2 is winner")
# elif P1_input.upper() == 'WATER' and P2_input.upper() == 'GUN':
#     print(f"P1 is winner")
# elif P1_input.upper() == 'GUN' and P2_input.upper() == 'SNAKE':
#     print(f"P1 is winner")
# elif P1_input.upper() == 'GUN' and P2_input.upper() == 'WATER':
#     print(f"P2 is winner")
# elif P1_input.upper() == P2_input.upper():
#     print(f"P1 and P2 both have selected same. Try again")


#Better way 

rules = {

    "SNAKE" : "GUN",
    "WATER" : "SNAKE",
    "GUN"   : "WATER"
}

# P1_input = input("Enter P1's choice : ").upper()
# P2_input = input("Enter P2's choice : ").upper()

# if P1_input not in rules or P2_input not in rules:
#     print(f"Invalid choices")
# elif P1_input == P2_input:
#     print(f"choices are same")
# elif rules[P1_input] != P2_input:
#     print(f"P1 Wins")
# else:
#     print(f"P2 Wins")


while 1:
    P1_input = input("Enter P1's choice : ").upper().strip()
    P2_input = input("Enter P2's choice : ").upper().strip()
    if P1_input not in rules or P2_input not in rules :
        print(f"Invalid choices Enter again")
    elif P1_input == P2_input:
        print(f"choices are same Enter again")
    else:
        break
    
if rules[P1_input] != P2_input:
    print(f"P1 Wins")
else:
    print(f"P2 Wins")

