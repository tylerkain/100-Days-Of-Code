#!/usr/bin/ env python3
import random

"""Variables"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = True

game_choices = [rock, paper, scissors]


while game: 

    user_choice = int(input("[+] Choices \n 0: Rock \n 1: Paper \n 2: Scissors \n User Input: "))
    computer_choice= game_choices[random.randint(0,2)]
    player_choice = game_choices[user_choice]

    if user_choice >= 3 or user_choice < 0: 
        print("You typed an invalid number, you lose!")
        game = False
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
        game = False
    elif computer_choice > user_choice:
        print("You lose")
        game = False
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")