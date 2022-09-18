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

if ch == "1":
    add(fnum, snum)
elif ch == "2":
    sub(fnum, snum)
elif ch == "3":
    div(fnum, snum)
elif ch == "4":
    mul(fnum, snum)
else:
    print("Invalid Choice...")