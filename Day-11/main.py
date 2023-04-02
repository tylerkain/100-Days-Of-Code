#!/bin/usr/env python3
from card_game import deal_card, user_cards, dealer_cards, calc_sum
from art import logo

print(logo)
deal_card()

wins = 0
for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

calc_sum(user_cards, dealer_cards, wins )

