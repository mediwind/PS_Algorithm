import sys
input = sys.stdin.readline

N = int(input())
works = list()
for _ in range(N):
    a, b = map(int, input().split())
    works.append([b - a + 1, b])
works.sort(key = lambda x: -x[1])

for i in range(1, N):
    prev_start, now_end = works[i - 1][0], works[i][1]
    if prev_start <= now_end:
        fixed_now_end = (prev_start - 1)
        works[i][1], works[i][0] = fixed_now_end, fixed_now_end - (works[i][1] - works[i][0])

print(works[-1][0] - 1)