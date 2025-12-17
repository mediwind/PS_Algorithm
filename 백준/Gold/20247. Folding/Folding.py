import sys
input = sys.stdin.readline

p1, q1, p2, q2 = map(int, input().strip().split())
q = int(input().strip())

def image(a, b, x):
    if b <= x:
        l = x - b
        r = x - a
    elif a >= x:
        l = a - x
        r = b - x
    else:
        l = 0
        r = max(x - a, b - x)
    return l, r

out = []
for _ in range(q):
    x = int(input())
    l1, r1 = image(p1, q1, x)
    l2, r2 = image(p2, q2, x)
    len1 = r1 - l1
    len2 = r2 - l2
    inter = max(0, min(r1, r2) - max(l1, l2))
    total = len1 + len2 - inter
    print(total)