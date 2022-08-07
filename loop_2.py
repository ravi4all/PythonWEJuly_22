num = int(input("Enter a number : "))

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

sum = 0
for i in range(1, num + 1):
    sum = sum + i

print("Sum is",sum)
