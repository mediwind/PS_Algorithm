def solution(friends, gifts):
    n = len(friends)
    name_dict = {val:idx for idx, val in enumerate(friends)}
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # gifts로 board 채우기
    for gift in gifts:
        a, b = gift.split()
        board[name_dict[a]][name_dict[b]] += 1 # 받은 사람 += 1
    
    # 선물 지수 구하기
    gift_index = [[0 for _ in range(3)] for _ in range(n)]
    rotated = list(zip(*board))
    for v in name_dict.values():
        gift_index[v][0] = sum(board[v])
        gift_index[v][1] = sum(rotated[v])
        gift_index[v][2] = gift_index[v][0] - gift_index[v][1]
    
    res = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if board[i][j] > board[j][i]:
                res[i] += 1
            elif board[i][j] == board[j][i]:
                if gift_index[i][2] > gift_index[j][2]:
                    res[i] += 1
        
    answer = max(res)
    return answer