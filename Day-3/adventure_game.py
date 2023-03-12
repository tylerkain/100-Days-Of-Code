#!/usr/bin/env python3

print("Welcome To Treasue Island")
print("[+] Your at a crossroads where do you go: \n [1] The Shores of the Island \n [2] The Island Jungle")
'''Variables'''
user_input = input("[+] Input 1 or 2: ")


if user_input == "1": 
    choice = input("You have arrived at the Shore of the Island \n [1]: Wait for the boat to the other island \n [2]: Swim to the island \n Choice 1 or 2: ")
    if choice == "1": 
        print(" You crossed the sea succesfully and found the treasure")
    elif choice == "2": 
        print(" You Drowned in the rough sea, \n GAME OVER!!!")

