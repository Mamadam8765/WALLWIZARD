import json
import uuid
import re
import time
import keyboard
import os
import hashlib
import random
from rich.console import Console


console = Console()

logo = r"""
 __      __        .__  .__     __      __.__                         .___
/  \    /  \_____  |  | |  |   /  \    /  \__|____________ _______  __| _/
\   \/\/   /\__  \ |  | |  |   \   \/\/   /  \___   /\__  \\_  __ \/ __ | 
 \        /  / __ \|  |_|  |__  \        /|  |/    /  / __ \|  | \/ /_/ | 
  \__/\  /  (____  /____/____/   \__/\  / |__/_____ \(____  /__|  \____ | 
       \/        \/                   \/           \/     \/           \/ 
"""


board_template = (
    "#####################################\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#---+---+---+---+---+---+---+---+---#\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#---+---+---+---+---+---+---+---+---#\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#---+---+---+---+---+---+---+---+---#\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#---+---+---+---+---+---+---+---+---#\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#---+---+---+---+---+---+---+---+---#\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#---+---+---+---+---+---+---+---+---#\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#---+---+---+---+---+---+---+---+---#\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#---+---+---+---+---+---+---+---+---#\n"
    "# ● | ● | ● | ● | ● | ● | ● | ● | ● #\n"
    "#####################################\n"
)
count_player1_wall = 0
count_player2_wall = 0

i1 = 56 
i2 = 664  
x = 76  
blue = "[2196f3]"
pink = "[ff69eb]"
down_index = [648 , 652 , 656 , 660 , 664 , 668 , 672 , 676 , 680]
up_index = [40 , 44, 48 , 52 , 56 , 60 , 64 , 68 , 72]
console = Console()
visited1 = []
visited2 = [] 
count_1 = 0
count_2 = 0
t = True

def clear_terminal_after_delay():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print each character with a small delay and style
for char in logo:
    console.print(char, style="#2196f3", end="")
    time.sleep(0.005)  # Adjust the delay time for typing effect
print("")

time.sleep(3)
clear_terminal_after_delay()

def delay_with_countdown():
    for i in range(3, 0, -1):
        print(f"Wait for {i}...")
        time.sleep(1)
    print("Done!")


# function for reading data we need to use
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# function that we use to check email pattern we use while to run the loop until user enter the cuurect pattern
def check_email():
    while True:
        email = input("Enter your email: ")
        print("")
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        else:
            print("Invalid email format. Please try again.")
            print("")

# function to check password length we use while to run the loop until user enter the cuurect pattern
def check_password():
    while True:
        password = input("Enter your password: ")
        password = password.encode('utf-8')
        password = hashlib.sha256(password).hexdigest()
        print("")
        if len(password) >= 8:
            return password
        else:
            print("Password must be at least 8 characters long. Please try again.")
            print("")

# function for saving users data
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# loading last data from users
users = load_users()

def display_menu_p1(options, selected):
    for i, option in enumerate(options):
        if i == selected:
            print(f"\033[48;2;33;150;243m{option}\033[0m")  # نمایش رنگ انتخاب‌شده
        else:
            print(option)


def display_menu_p2(options, selected):
    for i, option in enumerate(options):
        if i == selected:
            print(f"\033[48;2;255;105;235m{option}\033[0m") # نمایش رنگ انتخاب‌شده
        else:
            print(option)

def choice1_menuـp1():
    options = ["    (LOGIN)", "", "        (SIGNUP)" , "" , "              (EXIT)"]
    selected = 0

    while True:
        print("\033c", end="")  # Clear screen
        print("Player 1 -- > Use arrow keys to select and press E:\n")
        display_menu_p1(options, selected)
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN and event.name == 'down':
            selected = (selected + 2) % len(options)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'up':
            selected = (selected - 2) % len(options)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'e':
            print("")
            return selected

def choice1_menuـp2():
    options = ["    (LOGIN)", "", "        (SIGNUP)" , "" , "              (EXIT)"]
    selected = 0

    while True:
        print("\033c", end="")  # Clear screen
        print("Player 2 -- > Use arrow keys to select and press E:\n")
        display_menu_p2(options, selected)
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN and event.name == 'down':
            selected = (selected + 2) % len(options)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'up':
            selected = (selected - 2) % len(options)
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'e':
            print("")
            return selected



# signup or login section for player 1
def login_signup_player1(choice1):
    user_id = None
    if choice1 == 2 :
        # getting email and password from user 1
        email = check_email()
        password = check_password()

        # check if the email is unique
        if email in users:
            print("This email already exists. \n")
            email = check_email()
        else:
            # generating uuid for new users
            user_id = str(uuid.uuid4())
            # saving new users data
        users[email] = {
            "id": user_id,
            "email": email,
            "password": password
        }
        
        save_users(users)
        print("User registered successfully.\n")
        
    elif choice1 == 0 :

        # LOGIN process
        email = check_email()

        if email in users:
            password = input("Enter your password: ")
            password = password.encode('utf-8')
            password = hashlib.sha256(password).hexdigest()

            print("")
            if password == users[email]["password"]:
                print("Player 1 -- > You have successfully logged in!")
                print("")
            else:
                print("Incorrect password. Please try again.")
                delay_with_countdown()
                print("")
                choice1 = choice1_menuـp1() 
                login_signup_player1(choice1)
        else:
            print("No account found with this email. Please sign up. \n")
            delay_with_countdown()
            print("")
            choice1 = choice1_menuـp1() 
            login_signup_player1(choice1)
    elif choice1 == 4 :
        exit()

# signup or login section for player 2
def login_signup_player2(choice2):
    if choice2 == 2 :
        # getting email and password from user 1
        email = check_email()
        password = check_password()

        # check if the email is unique
        if email in users:
            print("This email already exists. \n")
            email = check_email()
        else:
            # generating uuid for new users
            user_id = str(uuid.uuid4())
            # saving new users data
        users[email] = {
            "id": user_id,
            "email": email,
            "password": password
        }
        
        # saving new users data in json file
        save_users(users)
        print("User registered successfully. \n")
        for i in range(3, 0, -1):
            print(f"Game will start in {i}...")
            time.sleep(1)
        print("Done! \n")
        clear_terminal_after_delay()
    elif choice2 == 0 :

        # LOGIN process
        email = check_email()

        if email in users:
            password = input("Enter your password: ")

            password = password.encode('utf-8')
            password = hashlib.sha256(password).hexdigest()
            print("")
            if password == users[email]["password"]:
                print("Player 2 -- > You have successfully logged in!\n")
                for i in range(3, 0, -1):
                    print(f"Game will start in {i}... \n")
                    time.sleep(1)
                print("Done! \n")
                clear_terminal_after_delay()
                
            else:
                print("Incorrect password. Please try again.")
                delay_with_countdown()
                print("")
                choice2 = choice1_menuـp2() 
                login_signup_player2(choice2)
        else:
            print("No account found with this email. Please sign up.")
            delay_with_countdown()
            print("")
            choice2 = choice1_menuـp2() 
            login_signup_player2(choice2)
    elif choice2 == 4 :
        exit()
