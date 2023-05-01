#!/usr/bin/env python3
"""Modules"""
import random

from hangman_art import stages
from words import word_list

'''Variables'''
word_list = word_list
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
user_lives = 6
game = False

for _ in range(word_length):
    display += "_"

while not game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        user_lives -= 1
        if user_lives == 0:
            game = True
            print("You Lost")
    print(f"{''.join(display)} \n Lives Remaining: {user_lives}")

    if "_" not in display:
        print("You Win")
        game = True

    print(stages[user_lives])
