from datetime import datetime as dt
import os, random

name = input("Enter your name : ")

greetIntent = ["hi", "hey", "hello", "hello there", "hi there", "hey there"]
dateIntent = ["date", "what's the date", "tell me date"]
musicIntent = ["play music", "start music", "play song"]
timeIntent = ["time", "what's the time", "tell me time"]

# Membership Operators : in, not in

chat = True
while chat:
    msg = input("User Message : ")

    if msg in greetIntent:
        print(f"CPU : Hello {name}")
    elif msg in dateIntent:
        current_date = dt.now().date()
        print(current_date.strftime("%a, %d %b, %y"))
    elif msg in timeIntent:
        current_time = dt.now().time()
        print(current_time.strftime("%I:%M:%S,%p"))
    elif msg in musicIntent:
        path = "D:/Batches/Songs"
        songs = os.listdir(path)
        song = random.choice(songs)
        song_to_play = path + "/" + song
        print("Playing :",song_to_play)
        os.startfile(song_to_play)
    elif msg == "bye":
        chat = False
    else:
        print("I don't Understand...")
