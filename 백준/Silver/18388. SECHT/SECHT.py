code = {
    "Q": "W",
    "W": "E",
    "E": "R",
    "R": "T",
    "T": "Y",
    "Y": "U",
    "U": "I",
    "I": "O",
    "O": "P",
    "A": "S",
    "S": "D",
    "D": "F",
    "F": "G",
    "G": "H",
    "H": "J",
    "J": "K",
    "K": "L",
    "Z": "X",
    "X": "C",
    "C": "V",
    "V": "B",
    "B": "N",
    "N": "M"
}

encoded = input()
decoded = ""
for char in encoded:
    if char.isalpha():
        if char in code:
            decoded += code[char]
        else:
            decoded += char
    else:
        decoded += char

print(decoded)