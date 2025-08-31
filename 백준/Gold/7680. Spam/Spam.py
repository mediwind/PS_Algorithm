import sys
input = sys.stdin.readline

spam_alphabet = {
    'A': "4", 'B': "|3", 'C': "(", 'D': "|)", 'E': "3", 'F': "|=",
    'G': "6", 'H': "#", 'I': "|", 'J': "_|", 'K': "|<", 'L': "|_",
    'M': "|\\/|", 'N': "|\\|", 'O': "0", 'P': "|0", 'Q': "(,)",
    'R': "|?", 'S': "5", 'T': "7", 'U': "|_|", 'V': "\\/", 'W': "\\/\\/",
    'X': "><", 'Y': "-/", 'Z': "2"
}

while True:
    s = input().rstrip()
    if s == "end":
        break

    t = ""
    for char in s:
        t += spam_alphabet[char]

    c = [0 for _ in range(len(t) + 1)]
    c[0] = 1

    for i in range(1, len(t) + 1):
        for char, encoding in spam_alphabet.items():
            if i >= len(encoding) and t[:i].endswith(encoding):
                c[i] += c[i - len(encoding)]

    print(c[len(t)])