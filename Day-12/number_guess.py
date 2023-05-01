#!/bin/usr/env python3
import random


def check_guess(user_answer, computer_answer):
    """Check guess based on level of difficulty"""
    if user_answer > computer_answer:
        print("Guess is to High")
    elif user_answer < computer_answer:
        print("Guess is to Low")
    else:
        print(f"You got the answer:{computer_answer}")


def game():
    answer = random.randint(1, 100)
    print("Guess a number between 1-100: ")
    user_guess = 0
    while user_guess != answer:
        user_guess = int(input("Make a guess: "))
        check_guess(user_guess, answer)


game()
