# - Map - Maps a function to a list of items. Tranforms every item

l = [1,2,3,4,5,4,3,2]
newl = list(map(lambda x: x*x*x, l))
print(newl)

print(list(map(lambda x: x + 1, [])))
# - Filter - Filter out the elements needed. Keep only items that match a condition 

fl = list(filter(lambda x: x>2,l))
print(fl)
print(list(filter(lambda x: '', [10, 20, 30])))
# - What happens if you call list() on the same map iterator twice?
m = map(lambda x: x * 2, [1, 2])
print(list(m))
print(list(m))
# - The first list(m) consumes the iterator and produces [2, 4].
# - Once those elements have been consumed, there are no elements left for the second call. So it produces [].
numbers = [2, 4, 6]
result = map(lambda x: x // 2, numbers)
print(list(result))
print("===========================")


# - Reduce - Combine items into one result
from functools import reduce
r = reduce(lambda x,y:x+y,l)
print(r)

print(list(filter(lambda x: x * 1, [0, 1, 2, 3])))

print(reduce(lambda a, b: a - b, [20, 5, 3]))

print(reduce(lambda a, b: a - b, [3, 5, 20]))




# - Using filter(), keep only prices greater than 100, then use map() to apply a 10% discount to each remaining price. Print the final list.

prices = [120, 250, 80, 400, 150]
discounted_prices = list(map(lambda x: x*.90 ,filter(lambda x : x> 100,prices)))
print(discounted_prices)


# - Write a program that:
# 1. Uses filter() to keep sales greater than or equal to 100.
# 2. Uses map() to apply a 10% increase to each qualifying sale.
# 3. Uses reduce() to calculate the total of the increased sales.

sales = [100, 250, 80, 400, 150, 50]

amplified_sales = list(map(lambda x: x*1.10 ,filter(lambda x : x>= 100,sales)))
total_increased_sales = reduce(lambda x,y : x+y ,amplified_sales)
print(f"total_increased_sales : {total_increased_sales}")


# - Write a program that:
# 1. Keeps transactions strictly greater than 500.
# 2. Applies a 5% discount to each qualifying transaction.
# 3. Calculates the average discounted transaction value, but prints "No qualifying transactions" when none exist.

transactions = [100, 450, 2000, 75, 300, 150]
discounted_transactions = list(map(lambda x: x*.95 ,filter(lambda x : x> 500,transactions)))
average_discounted_transaction_value = reduce(lambda x,y : (x+y),discounted_transactions)/len(discounted_transactions) if len(discounted_transactions) > 0 else "No qualifying transactions"
print(f"average_discounted_transaction_value : {average_discounted_transaction_value}")



