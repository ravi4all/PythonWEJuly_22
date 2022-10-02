def atm():
    total = 12000
    pin = input("Enter your pin : ")
    if pin == "1234":
        print("Login Success...")
    else:
        raise ValueError("Login Failed...")

    amount = int(input("Enter amount to withdraw : "))
    if amount > total:
        raise ValueError("Insufficient Balance...")

    total -= amount
    print("Remaining balance is",total)

try:
    atm()
except ValueError as msg:
    print(msg)