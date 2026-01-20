import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = list()
    
for k in range(2, N + 2):
    ans.append(k * M)

print(*ans)