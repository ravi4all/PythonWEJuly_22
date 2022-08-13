import random

cpu = random.randint(1,100)

counter = 0
while True:
    guess = int(input("Enter your guess : "))
    if cpu == guess:
        print("Congrats, You have guessed the number...")
        break
    elif cpu > guess:
        print("You have entered smaller number")
    elif cpu < guess:
        print("You have guessed larger number")
    counter += 1
    if counter == 5:
        print("You lost the game, Number was :",cpu)
        break