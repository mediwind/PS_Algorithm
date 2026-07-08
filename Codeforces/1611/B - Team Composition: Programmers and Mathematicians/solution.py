import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    teams = (a + b) // 4
    teams = min(teams, min(a, b))
    print(teams)