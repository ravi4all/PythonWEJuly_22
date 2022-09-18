def calc(x,y,opr):
    expression = x + opr + y
    z = eval(expression)
    print("Result is",z)

print("""
1. Addition
2. Subtraction
3. Division
4. Multiplication
""")

ch = input("Enter your choice : ")

fnum = input("Enter first num : ")
snum = input("Enter second number : ")

operations = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "*"
}
operator = operations.get(ch)
calc(fnum, snum, operator)