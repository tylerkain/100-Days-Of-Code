"""Modules"""
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
game_lives = 5
user_lives = 1
game = False

for _ in range(word_length):
    display += "_"

while not game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        else:
            user_lives += 1
    print(display)

    if "_" not in display:
        print("You Win")
        game = True


