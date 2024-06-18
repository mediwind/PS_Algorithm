def moving(x):
    if A1 <= x <= A2:
        x = A1 + A2 - x
    if B1 <= x <= B2:
        x = B1 + B2 - x
    return x


N, K = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

answer = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    cur = moving(i) # 일단 1턴 움직입니다.
    needed_turn = 1 # 그래서 1
    while cur != i: # 다시 제자리로 돌아올 때까지
        cur = moving(cur)
        needed_turn += 1 # 턴을 늘리며 움직입니다.
    k = K % needed_turn
    
    cur = i
    for _ in range(k):
        cur = moving(cur)
    answer[cur] = i

for ans in answer[1:]:
    print(ans)