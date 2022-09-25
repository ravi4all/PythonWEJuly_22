# positions = [i for i in range(0,9)]

positions = [""] * 9
def gameBoard():
    print("""
    {} | {} | {}
    -----------
    {} | {} | {}
    -----------
    {} | {} | {}
    """.format(positions[0], positions[1], positions[2],
    positions[3], positions[4], positions[5],
    positions[6], positions[7], positions[8]))

def checkWinner():
    pass

def userMove(user_ch):
    pos = int(input("Enter your position : "))
    positions[pos] = user_ch

def cpuMove(cpu_ch):
    pass

def game():
    gameBoard()
    user_choice = input("Enter your choice : 0/X : ")
    if user_choice == "X":
        cpu_choice = "0"
    else:
        cpu_choice = "X"

    userMove(user_choice)
    gameBoard()
    cpuMove(cpu_choice)
    # gameBoard()

game()
