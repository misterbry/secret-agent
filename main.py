#!/usr/local/bin/python

from time import sleep
import os
from playsound import playsound

secret_message = "Renegade seagulls have been spotted in the upper yard. Exercise caution, DO NOT APPROACH."
password = "password"
program_is_running = True
sounds = ['/audio/heal.wav', '/audio/sword.wav', '/audio/main.ogg', '/audio/death.wav']

def main():
    os.system("clear")
    login()
    while program_is_running:
        passwd()

def login():
    name = input("Welcome to the Intergalactic Bureau of Intelligence. Please enter your name. >>> ")
    os.system("clear")
    welcome_message = f"Hello special agent {name}. We have a secret message for you.\n\n"
    print(welcome_message)    

def passwd():
    user_input = input("What's the password? >>> ")
    if user_input == password:
        os.system("clear")
        print("Password is a match, decoding secret message...")
        sleep(2)
        os.system("clear")
        print(secret_message)
        print("\n")
        global program_is_running
        program_is_running = False

    else:
        os.system("clear")
        print("Password incorrect, try again.\n\n")
        passwd()

if __name__ == '__main__':
    main()
