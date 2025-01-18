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
