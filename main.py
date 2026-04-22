import os

import chr_creation

def main():
    while True:
        os.system("cls")
        print("------------------")
        print("AI Text Adventure")
        print("------------------")
        print("New Game")  #Goes to character creation module
        print("Load Game") #Goes to load game module
        print("Settings")  #Goes to game_settings module
        print("Help")      #Goes to help module
        print("Exit")      #Exits game
        print("")
        user_input = input("Enter: ").lower().strip()
        if user_input == "n" or user_input == "ng" or user_input == "new" or user_input == "new game":
            print("new")
            input("Press 'Enter' to continue")
            chr_creation.start()
        elif user_input == "l" or user_input == "lg" or user_input == "load" or user_input == "load game":
            print("load")
            input("Press 'Enter' to continue")
        elif user_input == "s" or user_input == "set" or user_input == "sett" or user_input == "setting" or user_input == "settings":
            print("settings")
            input("Press 'Enter' to continue")
        elif user_input == "h" or user_input == "help":
            print("help")
            input("Press 'Enter' to continue")
        elif user_input == "e" or user_input == "exit":
            input("Press 'Enter' to exit game")
            break
        else:
            print("Invalid option, try again!")
            input("Press 'Enter' to continue")
main()