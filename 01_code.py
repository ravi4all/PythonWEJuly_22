a = 17
b = 6
c = a + b
d = a - b
e = a / b
f = a * b
print(c)
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {2} is {0}".format(c,a,b))

print("Div of {} and {} is {:.2f}".format(a,b,e))

# f-strings - format strings
print(f"Sum of {a} and {b} is {c}")
print(f"Div of {a} and {b} is {e:.1f}")

#Multi-line print
print(f"""
Sum is {c}
Sub is {d}
Div is {e:.2f}
Mul is {f}
""")
