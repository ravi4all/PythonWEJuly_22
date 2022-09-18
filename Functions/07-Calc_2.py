def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Sub is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

print("""
1. Addition
2. Subtraction
3. Division
4. Multiplication
""")

ch = input("Enter your choice : ")

fnum = int(input("Enter first num : "))
snum = int(input("Enter second number : "))

# operations = [add,sub,div,mul]
# operations[int(ch) - 1](fnum, snum)

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}

operations.get(ch)(fnum, snum)

