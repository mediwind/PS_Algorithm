def DFS(L):
    global answer
    if L == 11:
        answer = max(answer, sum(scores))
#         print(sum(scores), *scores)
        return
    
    for i in range(11):
        if players[L][i] and not positions[i]:
            positions[i] = 1
            scores[i] = players[L][i]
            DFS(L + 1)
            positions[i] = 0
            scores[i] = 0
            
t = int(input())
for _ in range(t):
    # players = [
    #  [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 80, 70, 70, 60, 0, 0, 0, 0, 0, 0],
    #  [0, 40, 90, 90, 40, 0, 0, 0, 0, 0, 0],
    #  [0, 40, 85, 85, 33, 0, 0, 0, 0, 0, 0],
    #  [0, 70, 60, 60, 85, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 95, 70, 60, 60, 0, 0],
    #  [0, 45, 0, 0, 0, 80, 90, 50, 70, 0, 0],
    #  [0, 0, 0, 0, 0, 40, 90, 90, 40, 70, 0],
    #  [0, 0, 0, 0, 0, 0, 50, 70, 85, 50, 0],
    #  [0, 0, 0, 0, 0, 0, 66, 60, 0, 80, 80],
    #  [0, 0, 0, 0, 0, 0, 50, 50, 0, 90, 88]]
    players = [list(map(int, input().split())) for _ in range(11)]
    positions = [0 for _ in range(11)]
    scores = [0 for _ in range(11)]

    answer = float('-inf')
    DFS(0)
    print(answer)