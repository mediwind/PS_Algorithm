import sys
input = sys.stdin.readline


def need(width):
    # 색종이 폭이 width일 때, 다 덮기 위해 필요한 종이의 수
    prev = -1
    ret = 0
    for pos in arr:
        if prev == -1:
            # 처음 종이를 놓는 경우, [prev, prev+width) 까지 커버 가능
            prev = pos
            ret += 1
        elif prev + width <= pos:
            prev = pos
            ret += 1
    return ret

r, c = map(int, input().split())
n = int(input())
s = int(input())
spaces = [list(map(int, input().split())) for _ in range(s)]
arr = [col for row, col in sorted(spaces, key=lambda x: x[1])]

max_height = max(spaces, key=lambda x: x[0])[0]
l = max_height
r = 1000000  # range = [l, r]

while l < r:
    m = (l + r) // 2
    if need(m) <= n:
        # 가능한 경우
        r = m
    else:
        l = m + 1

print(l)