n = int(input())
cards = list(map(int, input().split()))
cards = [0] + cards

dy = [float('inf') for _ in range(n)]
dy = [0] + dy

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dy[i] = min(dy[i], dy[i - j] + cards[j])

print(dy[n])