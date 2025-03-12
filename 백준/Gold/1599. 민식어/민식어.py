import sys
input = sys.stdin.readline


def conversion(word):
    word = word.replace("ng", 'L')
    for k, v in dictionary.items():
        word = word.replace(k, v)
    return word


dictionary = {
    'a': 'A', 'b': 'B', 'k': 'C', 'd': 'D', 'e': 'E', 'g': 'F', 
    'h': 'G', 'i': 'H', 'l': 'I', 'm': 'J', 'n': 'K', 'o': 'M', 
    'p': 'N', 'r': 'O', 's': 'P', 't': 'Q', 'u': 'R', 'w': 'S', 'y': 'T'
}

n = int(input().rstrip())
words = [input().rstrip() for _ in range(n)]

pairs = dict()
for word in words:
    pairs[word] = conversion(word)

pairs = sorted(pairs.items(), key = lambda x: x[1])
for pair in pairs:
    print(pair[0])