# variable length arguments
def add(*x):
    # print(x)
    sum = 0
    for i in x:
        sum += i
    print("Sum is",sum)

add()
add(5)
add(4,5)
add(3,4,6)
add(3,2,4,6)
add(3,4,5,7,3,4,6,8)

# Keyword variable length argument
# **kwargs
def person(**details):
    print(details)

person(id=101, name="Ram")
person(name="Shyam", age=30, salary=45000)
person(id=103, name="John", age=31, salary=40000)
