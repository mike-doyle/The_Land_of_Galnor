import time, sys


# Welcome the new adventurer
print("")
# Use this block to delay text as if it is being typed
# text = "This is written slowly\n"
# for l in text:
#     sys.stdout.write(l)
#     sys.stdout.flush()
#     time.sleep(0.05)

def what_name(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)

def what_gender(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)

def what_status(string, delay):
    for char in string:
        time.sleep(delay)
        sys.stderr.write(char)

text = "           WELCOME TO THE LAND OF... "
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(2)
print(r"""
                                  ________       .__                       
                                 /  _____/_____  |  |   ____   ___________ 
                                /   \  ___\__  \ |  |  /    \ /  _ \_  __ \
                                \    \_\  \/ __ \|  |_|   |  (  <_> )  | \/
                                 \______  (____  /____/___|  /\____/|__|   
                                        \/     \/          \/              
      """)
#     v
print(r"""
                   /\                       /\                        /\                       /\
                  /**\                     /**\                      /**\                     /**\
                 /****\   /\      /\      /****\   /\               /****\   /\      /\      /****\   /\
                /      \ /**\    /  \    /      \ /**\             /      \ /**\    /  \    /      \ /**\
               /  /\    /    \  /    \  /  /\    /    \    /\     /  /\    /    \  /    \  /  /\    /    \
              /  /  \  /      \/      \/  /  \  /      \  /  \   /  /  \  /      \/      \/  /  \  /      \
             /  /    \/ /\     \      /  /    \/ /\     \/     \/  /    \/ /\     \      /  /    \/ /\     \
            /  /      \/  \/\   \    /  /      \/  \/\   \     /  /      \/  \/\   \    /  /      \/  \/\   \
         __/__/_______/___/__\___\__/__/_______/___/__\___\___/__/_______/___/__\___\__/__/_______/___/__\___\_
    """)

time.sleep(4)

text = "Welcome adventurer, to the land of Galnor!\nBefore we begin your journey, I have a few questions I need to ask in order to understand you a bit better.\n\n"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)

what_name("What is your name?\n>>> ",0.05)
name_enter = input()
text = "Very good! " + name_enter + "! It is a pleasure to meet your aquaintance.\n\n"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)

what_gender("Do you have a preferred pronoun?\n>>> ",0.05)
gender_select = input()
text = "Fantastic! ""'" + gender_select +"'" " I had a feeling, but I just wanted to be sure....\nYou look like a tiny shadow from way over here...\n\n"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(0.05)
text = "*The elderly man with the weary voice peers over at you, squinting his eyes*"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)
time.sleep(1)
print(r""" 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣄⠀⠀⠀⠀⠀⠀⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠀⠀⠀⠀⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡿⠿⠻⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⣶⡀⠀⠻⢛⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠈⣿⣷⠀⠀⠀⠀
⠀⠀⢠⣾⣿⣿⣿⣿⡦⣼⣯⣵⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⢹⣿⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⡿⣿⣿⣦⣀⢀⡘⣿⡇⠀⠀⠀
⠀⣾⣿⣿⣿⣿⡟⠉⠀⠀⣾⣿⣿⣿⣿⠟⠁⠀⠉⠻⣿⣿⣿⣿⣧⣠⣶⠄
⢰⣿⣿⣿⡿⠋⠀⠀⠀⢀⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠙⠻⣿⣿⣿⡟⠁⠀
⢸⣿⡿⠋⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠙⢻⡃⠀⠀
⠀⠁⠀⠀⠀⠀⠀⠀⣾⣿⣿⠿⣿⡿⢿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠙⢿⣿⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡟⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣾⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠘⠿⠿⠿⠀⠀⠀
      """)

time.sleep(0.05)
text = "Hmmm.... Needless to say, you will fit in quite well in Galnor!\n"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)

what_status("One more Question before I let you go,\nWere you raised very poor? Very Rich? Or somewhere in the middle?\n(Enter: Rich, Average, or Poor)>>> ",0.05)
status_select = input()
while True:
    try:
        status_select != str("rich")
    except ValueError:
        print("Sorry, I don't quite understand what you mean by that..")
        continue
    else:
        break
text = "So you grew up " "'"+ status_select + "'"" very interesting.\n\n"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)
text = "Well thats all the questions I have...\nFor now...\n\nI feel like its probably best I tell you that this is all a dream,\nyou really should wake up now...\n\n\n"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.08)

time.sleep(4)
print("Chapter 1: 'Bormand Trussle'\n\n")
text = "You awake suddenly from a nightmare.\nA storm settles in over the coastline as you rub your eyes.\n"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)
text = "As the moonlight peers through the small hut that you call home, leaks from the straw roof .\n"
for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.05)
