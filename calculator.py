def calculator(operation,a,b):
    if operation =='add':
        return a + b
    elif operation =='subtract':
        return a - b
    elif operation =='multiply':
        return a * b
    elif operation =='divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    


# Example usage:result_add = calculator('add', 10, 5)
print("Addition Result:", calculator('add', 10, 5))
print("Subtraction Result:", calculator('subtract', 10, 5))
print("Multiplication Result:", calculator('multiply', 10, 5))
print("Division Result:", calculator('divide', 10, 5))
print("Division by zero Result:", calculator('divide', 10, 0))
print("Invalid Operation Result:", calculator('modulus', 10, 5))