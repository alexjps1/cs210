import math

def encrypt(msg: str) -> str:
    evens = ''
    odds = ''
    extra = ''
    if len(msg) % 2 == 1:
        extra = msg[-1]
    for char_index in range(0, len(msg) - 1, 2):
        evens += msg[char_index]
        odds += msg[char_index + 1]
    return odds + evens + extra


def decrypt(msg: str) -> str:
    extra = ''
    if len(msg) % 2 == 1:
        extra = msg[-1]
        msg = msg[0:-1]
    middle = len(msg) // 2
    decrypted = ''
    for i in range(middle):
        decrypted += msg[middle + i] + msg[i]
    return decrypted + extra


def main():
    """Main program to run our encryption/decryption process."""

    which = input('Do you wish to encrypt or decrypt a message [E/D]? ')
    if which.upper() == 'E':
        text = input('Enter a line of text to encrypt: ')
        print("Encrypted text:")
        print(encrypt(text))
    elif which.upper() == 'D':
        text = input('Enter encrypted text to decrypt: ')
        print("Decrypted text:")
        print(decrypt(text))
    else:
        raise ValueError("Invalid option, I only know E and D!")


if __name__ == '__main__':
    main()
