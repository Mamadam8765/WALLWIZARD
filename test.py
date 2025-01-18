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

def player1_DFS(i1, visited1=None):
    global x
    if visited1 is None:
        visited1 = []  

    if i1 in down_index:  
        return True

    if i1 in visited1:
        return False


    visited1.append(i1)


    if board_template[i1 - 38] != "#" and (i1 - x) not in visited1:
        if player1_DFS(i1 - x, visited1):
            return True
    if board_template[i1 + 2] != "#" and (i1 + 4) not in visited1:
        if player1_DFS(i1 + 4, visited1):
            return True
    if board_template[i1 - 2] != "#" and (i1 - 4) not in visited1:
        if player1_DFS(i1 - 4, visited1):
            return True
    if board_template[i1 + 38] != "#" and (i1 + x) not in visited1:
        if player1_DFS(i1 + x, visited1):
            return True


    return False



def player2_DFS(i2 , visited2=None):
    global x

    if visited2 is None:
        visited2 = []

    if i2 in up_index:
        return True

    if i2 in visited2:
        return False

    visited2.append(i2)

    if board_template[i2 - 38] != "#" and (i2 - x) not in visited2:
        if player2_DFS(i2 - x , visited2):
            return True
    if board_template[i2 + 2] != "#" and (i2 + 4) not in visited2:
        if player2_DFS(i2 + 4 , visited2):
            return True
    if board_template[i2 - 2] != "#" and (i2 - 4) not in visited2:
        if player2_DFS(i2 - 4 , visited2):
            return True
    if board_template[i2 + 38] != "#" and (i2 + x) not in visited2:
        if player2_DFS(i2 + x , visited2):
            return True

    return False

def player1_action():
    global console, board_template , count_1
    if i1 in down_index:
        print("player_1 won the game !!!")
        exit()
    elif i2 in up_index:
        print("player_2 won the game !!!")
        exit()
    else :
        while i1 not in down_index:
            p1_input = input("player_1 => W = PLACE WALL , M = MOVE : ").lower()
            if p1_input == "exit":
                print("player_1 left the game !!!")
                exit()
            if p1_input == "m":
                m1 = input("player_1 => Enter your move (U, R, L, D): ").lower()
                check_walls_player1(m1)
                time.sleep(.7)
                clear_terminal_after_delay()
                console.print(update_board(i1, i2, x))
                player2_action()
            elif p1_input == "w":
                print(f"u put {count_1} walls in game")
                column1 = int(input("player_1 => Enter your column : "))
                row1 = int(input("player_1 => Enter your row : "))
                print("Hint => If you want to place down or up , the second part of the wall will be on left")
                print("Hint => If you want to place left or right , the second part of the wall will be on down")
                w1 = input("player_1 => Enter where do you want to place your wall (U , R , L , D) : ").lower()

                board_list = list(board_template)

                index = 38 + (76 * (row1 - 1)) + (4 * column1) - 2

                if w1 == "l": 
                    if board_list[index - 2] == "#" or board_list[index + 74] == "#":
                        print("There is already a wall there!")
                        player1_action()
                    if board_list[index + 38] == "#" and board_list[index + 34] == "#":
                        print("There is already a wall there!")
                        player1_action()

                    if count_1 < 10 :
                        board_list[index - 2] = "#"
                        board_list[index + 36] = "#"
                        board_list[index + 74] = "#"
                        count_1 += 1
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        print("u dont have wall !!!")
                        player1_action()

                    if not player2_DFS(i2):
                        print("You can't place the wall there, it blocks the path.")
                        count_1 -= 1
                        board_list[index - 2] = "|"
                        board_list[index + 36] = "+"
                        board_list[index + 74] = "|"
                        updated_board = ''.join(board_list)
                        board_template = updated_board

                    else:
                        time.sleep(.7)
                        clear_terminal_after_delay()
                        console.print(update_board(i1, i2, x))
                        player2_action()

                elif w1 == "r": 
                    if board_list[index + 2] == "#" or board_list[index + 78] == "#":
                        print("There is already a wall there!")
                        player1_action()
                    if board_list[index + 38] == "#" and board_list[index + 42] == "#":
                        print("there is wall !!!")
                        player1_action()
                    if count_1 < 10:
                        board_list[index + 2] = "#"
                        board_list[index + 40] = "#"
                        board_list[index + 78] = "#"
                        count_1 += 1
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else : 
                        print("u dont have wall !!!")
                        player1_action()

                    if not player2_DFS(i2):
                        print("You can't place the wall there, it blocks the path.")
                        count_1 -= 1
                        board_list[index + 2] = "|"
                        board_list[index + 40] = "+"
                        board_list[index + 78] = "|"
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        time.sleep(.7)
                        clear_terminal_after_delay()
                        console.print(update_board(i1, i2, x))
                        player2_action()

                elif w1 == "u":  
                    if board_list[index - 38] == "#":
                        print("There is already a wall there!")
                        player1_action()
                    if board_list[index - 40] == "#" :
                        print("There is already a wall there!")
                        player1_action()
                    if count_1 < 10:
                        board_list[index - 37] = "#"
                        board_list[index - 38] = "#"
                        board_list[index - 39] = "#"
                        board_list[index - 40] = "#"
                        board_list[index - 41] = "#"
                        board_list[index - 42] = "#"
                        board_list[index - 43] = "#"
                        count_1 += 1
                        updated_board = ''.join(board_list)
                        board_template = updated_board  
                    else:
                        print("u dont have wall !!!")
                        player1_action()


                    if not player2_DFS(i2):
                        print("You can't place the wall there, it blocks the path.")
                        count_1 -= 1
                        board_list[index - 37] = "-"
                        board_list[index - 38] = "-"
                        board_list[index - 39] = "-"
                        board_list[index - 40] = "+"
                        board_list[index - 41] = "-"
                        board_list[index - 42] = "-"
                        board_list[index - 43] = "-"
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        time.sleep(.7)
                        clear_terminal_after_delay()
                        console.print(update_board(i1, i2, x))
                        player2_action()

                elif w1 == "d":  
                    if board_list[index + 38] == "#":
                        print("There is already a wall there!")
                        player1_action()
                    if board_list[index + 36] == "#":
                        print("There is already a wall there!")
                        player1_action()
                    if count_1 < 10:
                        board_list[index + 38] = "#"
                        board_list[index + 37] = "#"
                        board_list[index + 39] = "#"
                        board_list[index + 36] = "#"
                        board_list[index + 35] = "#"
                        board_list[index + 34] = "#"
                        board_list[index + 33] = "#"
                        count_1 += 1
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        print("u dont have wall !!!")
                        player1_action()

                    if not player2_DFS(i2):
                        print("You can't place the wall there, it blocks the path.")
                        count_1 -= 1
                        board_list[index + 38] = "-"
                        board_list[index + 37] = "-"
                        board_list[index + 39] = "-"
                        board_list[index + 36] = "+"
                        board_list[index + 35] = "-"
                        board_list[index + 34] = "-"
                        board_list[index + 33] = "-"
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        time.sleep(.7)
                        clear_terminal_after_delay()
                        console.print(update_board(i1, i2, x))
                        player2_action()


def player2_action():
    global console, board_template , count_2
    if i1 in down_index:
        print("player_1 won the game !!!")
        exit()
    elif i2 in up_index:
        print("player_2 won the game !!!")
        exit()
    else:
        while i2 not in up_index:
            p2_input = input("player_2 => W = PLACE WALL , M = MOVE : ").lower()
            if p2_input == "exit":
                print("player_1 left the game !!!")
                exit()
            if p2_input == "m":
                m2 = input("player_2 => Enter your move (U, R, L, D): ").lower()
                check_walls_player2(m2)
                time.sleep(.7)
                clear_terminal_after_delay()
                console.print(update_board(i1, i2, x))
                player1_action()
            elif p2_input == "w":
                print(f"u put {count_2} walls in game")
                column2 = int(input("player_2 => Enter your column : "))
                row2 = int(input("player_2 => Enter your row : "))
                print("Hint => If you want to place down or up , the second part of the wall will be on left")
                print("Hint => If you want to place left or right , the second part of the wall will be on down")
                w2 = input("player_2 => Enter where do you want to place your wall (U , R , L , D) : ").lower()

                board_list = list(board_template)


                index = 38 + (76 * (row2 - 1)) + (4 * column2) - 2

                if w2 == "l": 
                    if board_list[index - 2] == "#" or board_list[index + 74] == "#":
                        print("there is wall !!!")
                        player2_action()
                    if board_list[index + 38] == "#" and board_list[index + 34] == "#":
                        print("There is already a wall there!")
                        player2_action()
                    if count_2 < 10:
                        board_list[index - 2] = "#"
                        board_list[index + 36] = "#"
                        board_list[index + 74] = "#"
                        count_2 += 1
                        updated_board = ''.join(board_list)
                        board_template = updated_board     
                    else:
                        print("u dont have wall !!!")
                        player2_action()      


                    if not player1_DFS(i1):  
                        print("You can't place the wall there, it blocks the path.")
                        count_2 -= 1
                        board_list[index - 2] = "|"
                        board_list[index + 36] = "+"
                        board_list[index + 74] = "|"
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        time.sleep(.7)
                        clear_terminal_after_delay()
                        console.print(update_board(i1, i2, x))
                        player1_action()

                elif w2 == "r": 
                    if board_list[index + 2] == "#" or board_list[index + 78] == "#":
                        print("there is wall !!!")
                        player2_action()
                    if board_list[index + 38] == "#" and board_list[index + 42] == "#":
                        print("there is wall !!!")
                        player2_action()
                    if count_2 < 10:
                        board_list[index + 2] = "#"
                        board_list[index + 40] = "#"
                        board_list[index + 78] = "#"
                        count_2 += 1
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        print("u dont have wall !!!")
                        player2_action()


                    if not player1_DFS(i1):  
                        print("You can't place the wall there, it blocks the path.")
                        count_2 -= 1
                        board_list[index + 2] = "|"
                        board_list[index + 40] = "+"
                        board_list[index + 78] = "|"
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        time.sleep(.7)
                        clear_terminal_after_delay()
                        console.print(update_board(i1, i2, x))
                        player1_action()

                elif w2 == "u": 
                    if board_list[index - 38] == "#":
                        print("There is already a wall there!")
                        player1_action()
                    if board_list[index - 40] == "#" :
                        print("There is already a wall there!")
                        player1_action()
                    if count_2 < 10:
                        board_list[index - 37] = "#"
                        board_list[index - 38] = "#"
                        board_list[index - 39] = "#"
                        board_list[index - 40] = "#"
                        board_list[index - 41] = "#"
                        board_list[index - 42] = "#"
                        board_list[index - 43] = "#"
                        count_2 += 1
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        print("u dont have wall !!!")
                        player2_action()

                    if not player1_DFS(i1): 
                        print("You can't place the wall there, it blocks the path.")
                        count_2 -= 1
                        board_list[index - 37] = "-"
                        board_list[index - 38] = "-"
                        board_list[index - 39] = "-"
                        board_list[index - 40] = "+"
                        board_list[index - 41] = "-"
                        board_list[index - 42] = "-"
                        board_list[index - 43] = "-"
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        time.sleep(.7)
                        clear_terminal_after_delay()
                        console.print(update_board(i1, i2, x))
                        player1_action()

                elif w2 == "d": 
                    if board_list[index + 38] == "#":
                        print("There is already a wall there!")
                        player1_action()
                    if board_list[index + 36] == "#":
                        print("There is already a wall there!")
                        player1_action()
                    if count_2 < 10:
                        board_list[index + 38] = "#"
                        board_list[index + 37] = "#"
                        board_list[index + 39] = "#"
                        board_list[index + 36] = "#"
                        board_list[index + 35] = "#"
                        board_list[index + 34] = "#"
                        board_list[index + 33] = "#"
                        count_2 += 1
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        print("u dont have wall !!!")
                        player2_action()

                    if not player1_DFS(i1):  
                        print("You can't place the wall there, it blocks the path.")
                        count_2 -= 1
                        board_list[index + 38] = "-"
                        board_list[index + 37] = "-"
                        board_list[index + 39] = "-"
                        board_list[index + 36] = "+"
                        board_list[index + 35] = "-"
                        board_list[index + 34] = "-"
                        board_list[index + 33] = "-"
                        updated_board = ''.join(board_list)
                        board_template = updated_board
                    else:
                        time.sleep(.7)
                        clear_terminal_after_delay()
                        console.print(update_board(i1, i2, x))
                        player1_action()





def update_board(i1, i2, x):
    if i2 > i1 :
        board = board_template[:i1] + "[#2196f3]●[/#2196f3]" + board_template[i1 + 1:i2] + "[#ff69eb]●[/#ff69eb]" + board_template[i2 + 1:]
        return board

    elif i1 > i2 :
        board = board_template[:i2] + "[#ff69eb]●[/#ff69eb]" + board_template[i2 + 1:i1] + "[#2196f3]●[/#2196f3]" + board_template[i1 + 1:]
        return board


def check_walls_player1(m1) :
    global i1 , x 
    while m1 not in ["u" , "d" , "l" , "r"]:
        print("wrong input")
        m1 = input("player_1 => Enter your move (U, R, L, D): ").lower()
    if m1 == "u" :
        if board_template[i1 - 38] == "#" :
            print("u cant go there !")
            m1 = input("player_1 => Enter your move (U, R, L, D): ").lower()
            check_walls_player1(m1)
        else : 
            player1_move(m1)
    elif m1 == "d" :
        if board_template[i1 + 38] == "#" :
            print("u cant go there !")
            m1 = input("player_1 => Enter your move (U, R, L, D): ").lower()
            check_walls_player1(m1)
        else : 
            player1_move(m1)
    elif m1 == "l" :
        if board_template[i1 - 2] == "#" :
            print("cant go there !")
            m1 = input("player_1 => Enter your move (U, R, L, D): ").lower()
            check_walls_player1(m1)
        else : 
            player1_move(m1)
    elif m1 == "r" :
        if board_template[i1 + 2] == "#" :
            print("u cant go there !")
            m1 = input("player_1 => Enter your move (U, R, L, D): ").lower()
            check_walls_player1(m1)
        else : 
            player1_move(m1)


def check_walls_player2(m2):
    global i2, x
    while m2 not in ["u" , "d" , "l" , "r"]:
        print("wrong input")
        m2 = input("player_2 => Enter your move (U, R, L, D): ").lower()
    
    if m2 == "u":
        if board_template[i2 - 38] == "#":
            print("You can't go there!")
            m2 = input("player_2 => Enter your move (U, R, L, D): ").lower()
            check_walls_player2(m2)
        else:
            player2_move(m2)
    elif m2 == "d":
        if board_template[i2 + 38] == "#":
            print("You can't go there!")
            m2 = input("player_2 => Enter your move (U, R, L, D): ").lower()
            check_walls_player2(m2)
        else:
            player2_move(m2)
    elif m2 == "l":
        if board_template[i2 - 2] == "#":
            print("You can't go there!")
            m2 = input("player_2 => Enter your move (U, R, L, D): ").lower()
            check_walls_player2(m2)
        else:
            player2_move(m2)
    elif m2 == "r":
        if board_template[i2 + 2] == "#":
            print("You can't go there!")
            m2 = input("player_2 => Enter your move (U, R, L, D): ").lower()
            check_walls_player2(m2)
        else:
            player2_move(m2)        

def player1_move(m1) :
    global i1 , x , i2
    if i1 in down_index:
        print("player_1 won the game !!!")
        exit()
    else:
        if m1 == "d":
            if i1 + x == i2:
                if board_template[i1 + 114] == "#":
                    user1_input = int(input("player_1 => u can go 1_(dow_left) or 2_(down_right) : "))
                    if user1_input == 1:
                        i1 += 72
                    elif user1_input == 2:
                        i1 += 80
                else:
                    i1 += 152
            else:
                i1 += x
        elif m1 == "u":
            if i1 - x == i2:
                if board_template[i1 - 114] == "#":
                    user1_input = int(input(print("player_1 => u can go 1_(up_left) or 2_(up_right) : ")))
                    if user1_input == 1:
                        i1 -= 80
                    elif user1_input == 2:
                        i1 -= 72
                else:
                    i1 -= 152
            else :
                i1 -= x
        elif m1 == "r":
            if i1 + 4 == i2:
                if board_template[i1 + 6] == "#":
                    user1_input = int(input(print("player_1 => u can go 1_(right_up) or 2_(right_down) : ")))
                    if user1_input == 1:
                        i1 -= 72
                    elif user1_input == 2:
                        i1 += 80
                else :
                    i1 += 8
            else:
                i1 += 4
        elif m1 == "l":
            if i1 - 4 == i2:
                if board_template[i1 - 6] == "#":
                    user1_input = int(input(print("player_1 => u can go 1_(left_up) or 2_(left_down) : ")))
                    if user1_input == 1:
                        i1 -= 80
                    elif user1_input == 2:
                        i1 += 80
                else:
                    i1 -= 8
            else:
                i1 -= 4



def player2_move(m2) :
    global i2 , x , i1
    if i2 in up_index:
        print("player_1 won the game !!!")
        exit()
    else:
        if m2 == "d":
            if i2 + x == i1:
                if board_template[i2 + 114] == "#":
                    user2_input = int(input("player_1 => u can go 1_(dow_left) or 2_(down_right) : "))
                    if user2_input == 1:
                        i2 += 72
                    elif user2_input == 2:
                        i2 += 80
                else:
                    i2 += 152
            else:
                i2 += x
        elif m2 == "u":
            if i2 - x == i1:
                if board_template[i2 - 114] == "#":
                    user2_input = int(input("player_1 => u can go 1_(up_left) or 2_(up_right) : "))
                    if user2_input == 1:
                        i2 -= 80
                    elif user2_input == 2:
                        i2 -= 72
                else:
                    i2 -= 152
            else :
                i2 -= x
        elif m2 == "r":
            if i2 + 4 == i1:
                if board_template[i2 + 6] == "#":
                    user2_input = int(input("player_1 => u can go 1_(right_up) or 2_(right_down) : "))
                    if user2_input == 1:
                        i2 -= 72
                    elif user2_input == 2:
                        i2 += 80
                else :
                    i2 += 8
            else:
                i2 += 4
        elif m2 == "l":
            if i2 - 4 == i1:
                if board_template[i2 - 6] == "#":
                    user2_input = int(input("player_1 => u can go 1_(left_up) or 2_(left_down) : "))
                    if user2_input == 1:
                        i2 -= 80
                    elif user2_input == 2:
                        i2 += 80
                else:
                    i2 -= 8
            else:
                i2 -= 4

choice1 = choice1_menuـp1()  
login_signup_player1(choice1)
time.sleep(2)
choice2 = choice1_menuـp2()  
login_signup_player2(choice2)


console.print(update_board(i1, i2, x))
first_player = random.randint(1 , 2)
if first_player == 1 :
    player1_action()
else :
    player2_action()