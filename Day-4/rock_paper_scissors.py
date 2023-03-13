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
computer_choices = [1, 2, 3]

while game: 

    user_choice = int(input("[+] Choices \n 1: Rock \n 2: Paper \n 3: Scissors \n User Input: "))
    computer_choice= game_choices[random.randint(0,2)]
    player_choice = game_choices[user_choice-1]

    if user_choice == computer_choice: