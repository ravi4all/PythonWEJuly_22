name = input("Enter Student Name : ")
eng = int(input("Enter English Marks : "))
phy = int(input("Enter Physics Marks : "))
math = int(input("Enter Maths Marks : "))
chem = int(input("Enter Chemistry Marks : "))
programming = int(input("Enter Programming Marks : "))

total = eng + phy + math + chem + programming
out_of = 500

percentage = total / out_of * 100 
print("Total Marks : {} out of 500".format(total))
print("Percentage is : {:.2f}".format(percentage))
