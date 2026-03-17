import sys
from collections import Counter
input = sys.stdin.readline


def comb2(x):
    return x * (x - 1) // 2


def comb3(x):
    return x * (x - 1) * (x - 2) // 6


team_name = input().strip()
n = int(input())

counter = Counter()

for _ in range(n):
    handle = input().strip()
    first_char = handle[0]
    counter[first_char] += 1

a, b, c = team_name[0], team_name[1], team_name[2]

if a == b == c:
    answer = comb3(counter[a])

elif a == b:
    answer = comb2(counter[a]) * counter[c]

elif b == c:
    answer = comb2(counter[b]) * counter[a]

elif a == c:
    answer = comb2(counter[a]) * counter[b]

else:
    answer = counter[a] * counter[b] * counter[c]

print(answer)