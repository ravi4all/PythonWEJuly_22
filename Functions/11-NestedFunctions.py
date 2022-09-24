def calc():
    x = 12
    y = 10
    # Nested Functions
    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    return add, sub

a, s = calc()
print(a())
print(s())
