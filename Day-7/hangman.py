"""Modules"""
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

user_guess = input("Guess a Letter: ").lower()

if user_guess in chosen_word:
    print("Letter is in random word")
else:
    print("letter is not in choosen word")
