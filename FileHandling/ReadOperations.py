# by default file opens in read mode
# file = open('notes.txt')
file = open('notes.txt','r')
# data = file.read()

# read 20 characters only
# data = file.read(20)

# start reading from 15th character
# file.seek(15)
# data = file.read(30)

# read first line only
# data = file.readline()

data = file.readlines()
print(data)
file.close()




