alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shifting(letter, value, process):
    if process == 1:
        if (letter + value) > 25:
            return alphabet[(letter+value) - 26]
        else:
            return alphabet[letter + value]
    elif process == 2:
        if (letter - value) < 0:
            return alphabet[(letter - value) + 26]
        else:
            return alphabet[letter - value]

def encrypt(text, shift):
    final = []
    for char in text:
        start = alphabet.index(char)
        end = shifting(start, shift, 1)
        final.append(end)
    return"".join(final)

def decrypt(text, shift):
    final = []
    for char in text:
        start = alphabet.index(char)
        end = shifting(start, shift, 2)
        final.append(end)
    return "".join(final)

while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(f"Your encrypted word is '{encrypt(text,shift)}'")
    elif direction == "decrypt":
        print(f"Your decrypted word is '{decrypt(text,shift)}'")
    
    again = input("\nWould you like to encrypt or decrypt again (y or n?) ")
    if again == "n":
        break
    