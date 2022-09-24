def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    # Packing
    return z1, z2, z3, z4

# Unpacking
add, sub, div, mul = calc(4,5)
print("Add is",add)
print("Sub is",sub)
print("Div is",div)
print("Mul is",mul)
