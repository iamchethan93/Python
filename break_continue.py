#While the code runs in a loop, we can exit/continue when the loop mets a particular condition.

for i in range (1,10):
    print(i)
    if i == 3:
        break


#Continue is for skipping the present iteration 

for i in range(12):
    if i == 10:
        print("Skipping 10")
        continue
    print("5 X", i, "=", 5*i)

