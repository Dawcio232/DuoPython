#Copyright 2026 @0verox - fake... unfortunatly...
#Here place imports
import time
from pathlib import Path
import os
#Here variables
score = 0
username = ""
sync = False
coins = 0
currentLevel = 0
currentLesson = 0
strInput = ""
intInput = 0
#Here dictionaries

#Here place functions
def syncData():
    global sync
    print("Loading data...")
    try:
        with open("data.txt", "r") as f:
            data = f.read().splitlines()
            global score, username, coins, currentLevel, currentLesson
            score = int(data[0])
            username = data[1]
            coins = int(data[2])
            currentLevel = int(data[3])
            currentLesson = int(data[4])
            sync = True
    except FileNotFoundError:
        print("No data file found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def initializeGame():
    print("Welcome to DuoPython!")
    time.sleep(2)
    if Path("data.txt").exists():
        print("Save detected.")
    else:
        print("No save detected.")
    intInput = input("Do you want to load your save? (1 for yes, 0 for no): ")
    if intInput == "1":
        syncData()
        if sync:
            print("Data loaded successfully.")
            return True
        else:
            print("Failed to load data.")
            initializeGame()
    elif intInput == "0":
        if Path("data.txt").exists():
            print("Starting a new game will overwrite your existing save.")
            intInput = input("Are you sure you want to continue? (1 for yes, 0 for no): ")
            if intInput == "1":
                print("Starting a new game...")
                score = 0
                username = input("Enter your username: ")
                coins = 0
                currentLevel = 0
                currentLesson = 0
                with open("data.txt", "w") as f:
                 f.write(f"{score}\n{username}\n{coins}\n{currentLevel}\n{currentLesson}")
                print("New game started.")
                return True
        else:
            print("Starting a new game...")
            score = 0
            username = input("Enter your username: ")
            coins = 0
            currentLevel = 0
            currentLesson = 0
            with open("data.txt", "w") as f:
                f.write(f"{score}\n{username}\n{coins}\n{currentLevel}\n{currentLesson}")
            print("New game started.")
            return True
    else:
        print("Invalid input. Please provide a valid response.")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        initializeGame()
#THE STARTUP SEQUENCE
initializeGame()
#yes... theres nothing else here...