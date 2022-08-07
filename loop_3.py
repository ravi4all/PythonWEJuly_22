num = 17

prime = True

for i in range(2,num):
    if num % i == 0:
        prime = False

if prime:
    print("Prime Number")
else:
    print("Not Prime")
