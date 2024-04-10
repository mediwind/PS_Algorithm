import sys
input = sys.stdin.readline

dy = [0 for _ in range(5001)]
dy[0] = 1
mod = 1000000007

for i in range(2, 5001, 2):
    for j in range(2, 5001, 2):
        dy[i] += dy[j - 2] * dy[i - j]
        dy[i] %= mod

t = int(input())
for _ in range(t):
    l = int(input())
    print(dy[l])