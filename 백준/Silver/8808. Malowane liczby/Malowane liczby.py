import sys
input = sys.stdin.readline


def color_of_fraction(a, b):
    s = 0
    while b:
        s += a // b
        a, b = b, a % b
        
    if s % 2 == 1:
        return "czerwony"
    else:
        return "niebieski"


Z = int(input().strip())
for _ in range(Z):
    line = input().strip()
    a, b = map(int, line.split('/'))
    print(color_of_fraction(a, b))