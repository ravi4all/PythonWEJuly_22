# Global variables - accessible throughout the program
x = 23
y = 22

# Function definition
def add():
    # Local Scope - variables cannot be accessed outside the function scope
    # x = 23
    # y = 22
    global z
    # make variables global that is defined inside local scope
    z = x + y
    print("Sum is",z)

def sub():
    # x = 23
    # y = 22
    global z
    z = x - y
    print("Sub is :",z)

# Function call
add()
sub()

print("Output is :",z)
