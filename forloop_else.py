#After the execution of all i iterables it goes for else block execution.
#Only after execution of iterations of for loop (very important).
for i in range(5):
    print(i)

else:
    print("No I")


#break will cause the else also to be skipped as the all the iterations of the for loop wil not be executed
for i in range(5):
    if i==2:
        break
    print(i)
else:
    print("No I")

