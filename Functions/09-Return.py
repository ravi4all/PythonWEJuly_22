# return - it is always last statement of a function
# we cannot write any code after return statement

def add(x,y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

def calc():
    z = add(12,4)
    print("Sum is",z)
    z = sub(10,5)
    print("Sub is",z)

calc()
