#Lambda is a small anonymous function without a name. It behaves as a function and can accpet single/multiple arguments.


def double(x):
    return x*2
print(double(5))

y = lambda a: a*2
print(y(5))

avg = lambda x,y:(x+y)/2
print(avg(1,2))
#We can call the lambda function similar to normal function

#Lambda is preferred over functions when they can used in a one liner or passed as a arguments.

f = lambda x: x * 2

print(f)


x = 10

f = lambda n: n + x

x = 20

print(f(5))

#Coding Challenge 1 — Temperature Converter
# - Create a lambda function named celsius_to_fahrenheit.
# - It should accept one parameter: the temperature in Celsius.
# - Use the formula:

# F = C *(9/5) + 32

fahrenheit = lambda c : c *(9/5) + 32

print(fahrenheit(25))

# - Coding Challenge 2 — Apply a Discount
# Write a lambda function named discounted_price that:
# - Accepts two parameters: price and discount.
# - Calculates the final price after applying the discount percentage.
# - Returns the calculated value through the lambda expression.
# For example, a price of 1000 with a discount of 20 should produce 800.0.

final_price = lambda p,d : p-(p*(d/100))

print(final_price(1000,20))

# Coding Challenge 3 — Conditional Lambda
# Now let's test whether you can use a conditional expression inside a lambda.

# Write a lambda function named check_number that:
# - Accepts one number.
# - Returns "Positive" if the number is greater than zero.
# - Returns "Not positive" otherwise.

check = lambda x : "Positive" if x > 0 else "Negative"
print(check(3))

# - Handle 3 conditions.
# - "Positive" if the number is greater than zero.
# - "Negative" if the number is less than zero.
# - "Zero" if the number equals zero.

# - Key takeaway: 
# - Nested conditional expressions are evaluated from left to right through the conditions: the first matching condition determines the result.
