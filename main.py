alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def forward(letter, value):
    if (letter + value) > 25:
        return alphabet[(letter+value) - 26]
    else:
        return alphabet[letter + value]

def encrypt(text, shift):
    final = []
    for char in text:
        start = alphabet.index(char)
        end = forward(start, shift)
        final.append(end)
    return"".join(final)

def reverse(letter, value):
    if (letter - value) < 0:
        return alphabet[(letter - value) + 26]
    else:
        return alphabet[letter - value]

def decrypt(text, shift):
    final = []
    for char in text:
        start = alphabet.index(char)
        end = reverse(start, shift)
        final.append(end)
    return"".join(final)

print(decrypt(text,shift))
