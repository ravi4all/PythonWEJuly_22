# file = open('file_1.txt', 'w')
# data = "Hello How are you...?"
# data = "ok I am fine..."

file = open('file_2.txt', 'x')
data = "\nThis is python programming...."
data = file.write(data)
print(data)
file.close()
