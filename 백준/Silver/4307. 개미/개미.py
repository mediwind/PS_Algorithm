import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, n = map(int, input().split())
    min_time = 0
    max_time = 0
    for _ in range(n):
        pos = int(input())
        sht = min(pos, l - pos)
        lng = max(pos, l - pos)
        min_time = max(min_time, sht)
        max_time = max(max_time, lng)
    print(min_time, max_time)