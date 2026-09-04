import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    A, B, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    total_damage = 0
    for i in range(n):
        rounds = (b[i] + A - 1) // A
        total_damage += rounds * a[i]
 
    max_a = max(a)
    if B - total_damage + max_a > 0:
        print("YES")
    else:
        print("NO")