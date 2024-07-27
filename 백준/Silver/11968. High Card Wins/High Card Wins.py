import sys
input = sys.stdin.readline

n = int(input())
deck = [0 for _ in range(n * 2 + 1)]
for _ in range(n):
    card = int(input())
    deck[card] = 1

bessie, elsie = list(), list()
for i in range(1, n * 2 + 1):
    if deck[i] == 1:
        elsie.append(i)
    else:
        bessie.append(i)

answer = 0
bp, ep = 0, 0
while ep < n and bp < n:
    if bessie[bp] > elsie[ep]:
        answer += 1
        bp += 1
        ep += 1
    elif bessie[bp] < elsie[ep]:
        bp += 1

print(answer)