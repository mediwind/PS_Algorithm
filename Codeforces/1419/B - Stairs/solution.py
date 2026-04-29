import sys
 
input = sys.stdin.readline
 
# 미리 nice staircase 비용들 생성
costs = []
k = 1
 
while True:
    stairs = (1 << k) - 1
    need = stairs * (stairs + 1) // 2
 
    if need > 10**18:
        break
 
    costs.append(need)
    k += 1
 
 
t = int(input())
 
for _ in range(t):
    x = int(input())
 
    answer = 0
 
    for need in costs:
        if x < need:
            break
 
        x -= need
        answer += 1
 
    print(answer)