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
    print("Wczytywanie danych...")
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
        print("Nie znaleziono pliku z danymi.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

def syncIn():
    with open("data.txt", "w") as f:
        f.write(f"{score}\n{username}\n{coins}\n{currentLevel}\n{currentLesson}")
    return "Dane zostały zsynchronizowane."

def initializeGame():
    os.system("cls" if os.name == "nt" else "clear")
    print("Witaj w DuoPython!")
    time.sleep(2)
    if Path("data.txt").exists():
        print("Znaleziono zapis.")
        print("Aby usunąć zapis, wpisz '2' w następnym pytaniu.")
    else:
        print("Nie znaleziono zapisu.")
    intInput = input("Czy chcesz wczytać zapis? (1 - tak, 0 - nie): ")
    if intInput == "1":
        syncData()
        if sync:
            print("Dane wczytano pomyślnie.")
            return True
        else:
            print("Nie udało się wczytać danych.")
            time.sleep(5)
            return initializeGame()
    elif intInput == "0":
        if Path("data.txt").exists():
            print("Rozpoczęcie nowej gry nadpisze istniejący zapis.")
            intInput = input('Czy na pewno chcesz kontynuować? \n Aby potwierdzić, wpisz "USUŃ MOJE PLIKI": ')
            if intInput == "USUŃ MOJE PLIKI":
                print("Rozpoczynanie nowej gry...")
                score = 0
                username = input("Podaj nazwę użytkownika: ")
                coins = 0
                currentLevel = 0
                currentLesson = 0
                with open("data.txt", "w") as f:
                 f.write(f"{score}\n{username}\n{coins}\n{currentLevel}\n{currentLesson}")
                print("Rozpoczęto nową grę.")
                return True
            else:
                print("Anulowano nową grę. Powrót do menu głównego.")
                time.sleep(5)
                return initializeGame()
        else:
            print("Rozpoczynanie nowej gry...")
            score = 0
            username = input("Podaj nazwę użytkownika: ")
            coins = 0
            currentLevel = 0
            currentLesson = 0
            with open("data.txt", "w") as f:
                f.write(f"{score}\n{username}\n{coins}\n{currentLevel}\n{currentLesson}")
            print("Rozpoczęto nową grę.")
            return True
    elif intInput == "2":
        if Path("data.txt").exists():
            intInput = input('Czy na pewno chcesz kontynuować? \n Aby potwierdzić, wpisz "USUŃ MOJE PLIKI": ')
            if intInput == "USUŃ MOJE PLIKI":
                os.remove("data.txt")
                print("Plik zapisu został usunięty.")
                time.sleep(5)
                return initializeGame()
            else:
                print("Anulowano usuwanie zapisu. Powrót do menu głównego.")
                time.sleep(5)
                return initializeGame()
        else:
            print("Brak pliku zapisu do usunięcia.")
            time.sleep(5)
            return initializeGame()
    else:
        print("Nieprawidłowa odpowiedź. Wprowadź poprawną wartość.")
        time.sleep(5)
        os.system("cls" if os.name == "nt" else "clear")
        return initializeGame()
#THE STARTUP SEQUENCE
os.system("cls" if os.name == "nt" else "clear")
if initializeGame() == True:
    print("Gra została pomyślnie uruchomiona.")
    os.system("cls" if os.name == "nt" else "clear")
else:
    print("Nie udało się uruchomić gry.")
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

print(f"Cześć! Jestem Lui! \n Witaj w Duo Python, {username}! \n Masz {coins} monet. \n Rozpocznijmy poziom {currentLevel}, lekcję {currentLesson}!")