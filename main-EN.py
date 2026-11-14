#Copyright 2026 @0verox - fake... unfortunatly...
#Here place imports
import time
from pathlib import Path
import os
import pygame
import sys
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
        print("Data file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def syncIn():
    with open("data.txt", "w") as f:
        f.write(f"{score}\n{username}\n{coins}\n{currentLevel}\n{currentLesson}")
    return "Data synchronized successfully."

def initializeGame():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to DuoPython!")
    time.sleep(2)
    if Path("data.txt").exists():
        print("Save file found.")
        print("To delete the save file, enter '2' at the next prompt.")
    else:
        print("No save file found.")
    intInput = input("Would you like to load the save? (1 - yes, 0 - no): ")
    if intInput == "1":
        syncData()
        if sync:
            print("Data loaded successfully.")
            return True
        else:
            print("Failed to load data.")
            time.sleep(5)
            return initializeGame()
    elif intInput == "0":
        if Path("data.txt").exists():
            print("Starting a new game will overwrite the existing save.")
            intInput = input('Are you sure you want to continue? \n To confirm, type "DELETE MY FILES": ')
            if intInput == "DELETE MY FILES":
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
                print("New game canceled. Returning to the main menu.")
                time.sleep(5)
                return initializeGame()
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
    elif intInput == "2":
        if Path("data.txt").exists():
            intInput = input('Are you sure you want to continue? \n To confirm, type "DELETE MY FILES": ')
            if intInput == "DELETE MY FILES":
                os.remove("data.txt")
                print("Save file deleted.")
                time.sleep(5)
                return initializeGame()
            else:
                print("Save deletion canceled. Returning to the main menu.")
                time.sleep(5)
                return initializeGame()
        else:
            print("There is no save file to delete.")
            time.sleep(5)
            return initializeGame()
    else:
        print("Invalid response. Enter a valid option.")
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        return initializeGame()
#THE STARTUP SEQUENCE
os.system("cls" if os.name == "nt" else "clear")
if initializeGame() == True:
    print("Game started successfully.")
    os.system("cls" if os.name == "nt" else "clear")
else:
    print("Failed to start the game.")
    exit()
if currentLesson == 0:
    currentLesson = 1
else:
    pass
if currentLevel == 0:
    currentLevel = 1
else:
    pass

print(syncIn())
#yes... theres nothing else here...

print(f"Hi! I'm Lui! \n Welcome to Duo Python, {username}! \n You have {coins} coins. \n Let's start level {currentLevel}, lesson {currentLesson}!")