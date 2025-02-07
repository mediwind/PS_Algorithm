import sys
input = sys.stdin.readline

n = int(input())

Q = list()
ans = 0
for _ in range(n):
    task = list(map(int, input().split()))
    
    if Q:
        Q[-1][1] -= 1
        if Q[-1][1] == 0:
            ans += Q[-1][0]
            Q.pop()
    
    if len(task) == 3:
        Q.append(task[1:])

if Q:
    Q[-1][1] -= 1
    if Q[-1][1] == 0:
        ans += Q[-1][0]
        Q.pop()

print(ans)