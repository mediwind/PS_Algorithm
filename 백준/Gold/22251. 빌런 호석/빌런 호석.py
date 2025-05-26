def counting(num1, num2):
    cnt = 0
    
    for i in range(7):
        if LED[num1][i] != LED[num2][i]:
            cnt += 1
    
    return cnt


LED = [
    [1, 1, 1, 0, 1, 1, 1], # 0
    [0, 0, 1, 0, 0, 1, 0], # 1
    [1, 0, 1, 1, 1, 0, 1], # 2
    [1, 0, 1, 1, 0, 1, 1], # 3
    [0, 1, 1, 1, 0, 1, 0], # 4
    [1, 1, 0, 1, 0, 1, 1], # 5
    [1, 1, 0, 1, 1, 1, 1], # 6
    [1, 0, 1, 0, 0, 1, 0], # 7
    [1, 1, 1, 1, 1, 1, 1], # 8
    [1, 1, 1, 1, 0, 1, 1] # 9
]

switch = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(i + 1, 10):
        switch[i][j] = switch[j][i] = counting(i, j)

N, K, P, X = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    if i == X:
        continue
    
    cnt = 0
    
    num1 = str(i).zfill(K)
    num2 = str(X).zfill(K)
    
    for j in range(K):
        cnt += switch[int(num1[j])][int(num2[j])]
            
    if cnt <= P:
        ans += 1

print(ans)