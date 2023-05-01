#!/usr/bin/ env python3
print("Welcome to Band Generator")


def band_name():
    """Band Name Generator"""
    city = input("What city did you grow up in: ")
    pet = input("What is the name of you pet: ")
    band_name = city + pet
    print(f' Band name is: {band_name}')


band_name()
