# def even(n):
#     return n % 2 == 0

numbers = [3,5,6,2,7,34,6,8,8,23,56,8,8,14,7,4]
# even(numbers[3])

# e = list(map(lambda n : n % 2 == 0, numbers))
e = list(filter(lambda n : n % 2 == 0, numbers))
print(e)
