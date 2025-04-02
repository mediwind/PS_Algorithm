import sys
input = sys.stdin.readline

c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

dy = [float("inf") for _ in range(c + 101)]
dy[0] = 0

for cost, customers in city:
    for i in range(customers, c + 101):
        dy[i] = min(dy[i], dy[i - customers] + cost)

print(min(dy[c:]))