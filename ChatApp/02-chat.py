name = input("Enter your name : ")

chat = True
while chat:
    msg = input("User Message : ")

    if msg == "hi" or msg == "hello" or msg == "hey" or msg == "hi there":
        print("CPU : Hello User")
    elif msg == "date" or msg == "tell me date" or msg == "what's the date":
        pass
    elif msg == "play music":
        chat = False
    elif msg == "tell me news":
        pass
    elif msg == "tell me about weather":
        pass
    elif msg == "bye":
        chat = False
    else:
        print("I don't Understand...")
