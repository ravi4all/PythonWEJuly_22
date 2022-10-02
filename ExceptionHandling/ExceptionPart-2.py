import io

try:
    file = open('file_1.txt', 'r')
    file.write("Hello World...")
except FileNotFoundError:
    print("File do not exist...")
    file = open('file_1.txt', 'w')
except io.UnsupportedOperation:
    print("Not supported operation...")
finally:
    print("I will always execute...")
    file.close()
    print("File Closed...")

