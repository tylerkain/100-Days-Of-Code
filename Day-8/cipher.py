import optparse

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_input():
    """Get input"""
    parser = optparse.OptionParser()
    parser.add_option("--text", dest="text",
                      help="text")
    parser.add_option("--shift", dest="shift",
                      help="shift amount")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify text, use --help")
    elif not options.mac:
        parser.error("[-] Please specify shift amount, use --help")
    return options


def encrypt(plain_text, shift_amount):
    """Encrypt Message"""
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    """Decrypt Message"""
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")