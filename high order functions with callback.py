numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(f"Squared numbers: {squared_numbers}")
# Using filter with a function as a callback
def is_even(num):
 return num % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(f"Even numbers: {even_numbers}")