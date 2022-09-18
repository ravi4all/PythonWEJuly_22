# Positional + Default
def calc(x,y,z=0):
    res = x + y + z
    print("Sum is",res)

calc(4,5)
calc(3,5,6)
# calc(z=12)
calc(x=3,y=3)
