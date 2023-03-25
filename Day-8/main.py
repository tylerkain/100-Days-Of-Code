#!/usr/bin/env python3
from cipher import decrypt, encrypt
cipher_program = False

while not cipher_program:
    """Variables"""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: type: 'exit' to close program\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
    if direction == 'decode':
        decrypt(text, shift)

