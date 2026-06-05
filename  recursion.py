# Calling a function inside a function.

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

#Fibonacci Sequence till given number.

#5 --> 0,1,1,2,3,5,8,13

def fibc(n):
    series = []
    
    for i in range(n):
        if i == 0:
            series.append(0)
            continue  
        elif i == 1:
            series.append(1)
            continue  
        else:
            x = series[-1] + series[-2]
            if x<n:
                series.append(x)
            else:
                break
    print(series)

fibc(15)

