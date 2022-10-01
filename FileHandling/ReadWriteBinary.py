file = open('img_1.png', 'rb')
data = file.read()
# print(data)
file.close()

file = open('img_2.png', 'wb')
file.write(data)
# file.write(data[:10000])
file.close()