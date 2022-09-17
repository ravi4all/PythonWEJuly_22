# Positional arguments
# def add(x,y):
#     z = x + y
#     print("Sum is",z)

# add(4,3)
# add(3,6)
# add(5,3)
# add(7,4)

# Invalid code
# add()
# add(4)

# Default arguments
def add(x=0,y=0):
    z = x + y
    print("Sum is",z)

# Keyword arguments
add(x=6, y=3)
add(y=4, x=12)

add()
add(4,6)
add(6)
