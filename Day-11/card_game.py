# Modules
import random

# Variables
user_cards = []
dealer_cards = []


# Functions
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_sum(user, dealer, games_won):
    games_won = 0
    user_total = sum(user)
    dealer_total = sum(dealer)
    if user_total == 21:
        print("Player Wins")
        games_won += 1
        print(f"Player wins: {games_won}")
    elif user_total < 21:
        print(user_total)
    if dealer_total == 21:
        print("Dealer Wins")
        games_won += 1
        print(f"Deal Wins: {games_won}")
    elif dealer_total < 21:
        print(dealer_total)


