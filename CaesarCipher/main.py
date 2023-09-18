import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        index = alphabet.index(char)
        cipher_text += alphabet[(index + shift) % 26]
    print(f"The encoded text is: {cipher_text}")


def decrypt(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        index = alphabet.index(char)
        plain_text += alphabet[(index - shift) % 26]
    print(f"The decoded text is: {plain_text}")


def caesar(text, shift, type_crypt):
    res = ""
    if type_crypt == 'decode':
        shift *= -1

    for char in text:
        index = alphabet.index(char)
        if index == -1:
            res += char
        else:
            res += alphabet[(index + shift) % 26]
    print(f"The {type_crypt}d text is: {res}")


def run_caesar():
    type_crypt = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input('Type your message: \n').lower()
    shift = int(input('Type the shift number: \n'))
    caesar(text, shift, type_crypt)


print(art.logo)
should_continue = True
while should_continue:
    run_caesar()
    again = input("Type 'yes' if you want to go again: \n")
    if again != 'yes':
        print("Goodbye!")
        should_continue = False
