#!/usr/bin/env python3
from caesar-cipher-art import logo
cipher = False


def caesar_cipher(plaintext, shift):
    """Encrypts plaintext using a Caesar cipher with the specified shift value"""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determine the new character code after applying the shift
            new_code = ord(char) + shift
            if char.isupper():
                # Handle uppercase letters
                new_code = (new_code - 65) % 26 + 65
            else:
                # Handle lowercase letters
                new_code = (new_code - 97) % 26 + 97
            ciphertext += chr(new_code)
        else:
            # Leave non-alphabetic characters unchanged
            ciphertext += char
    return ciphertext


def decrypt_caesar_cipher(ciphertext, shift):
    """Decrypts a message encrypted using a Caesar cipher with the specified shift value"""
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine the original character code before applying the shift
            original_code = ord(char) - shift
            if char.isupper():
                # Handle uppercase letters
                original_code = (original_code - 65) % 26 + 65
            else:
                # Handle lowercase letters
                original_code = (original_code - 97) % 26 + 97
            plaintext += chr(original_code)
        else:
            # Leave non-alphabetic characters unchanged
            plaintext += char
    return plaintext


print(logo)
while not cipher:
    direction = input("encode or decode: ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encode_message = caesar_cipher(plaintext=text, shift=shift)
        print(encode_message)
    elif direction == 'decode':
        decode_message = decrypt_caesar_cipher(ciphertext=text, shift=shift)
        print(decode_message)

    restart = input("Do you want to end the program: y/n: ")

    if restart == 'y':
        cipher = True

