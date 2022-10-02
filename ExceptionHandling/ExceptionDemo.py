try:
    fnum = int(input("Enter first num : "))
    snum = int(input("Enter second num : "))

    add = fnum + snum
    sub = fnum - snum
    div = fnum / snum
    mul = fnum * snum

except ZeroDivisionError:
    print("Cannot Divide by Zero...")

except ValueError:
    print("Invalid Input...Please enter a valid number")

except BaseException:
    print("Something went wrong...")

else:
    print("Sum is", add)
    print("Sub is", sub)
    print("Div is", div)
    print("Mul is", mul)
