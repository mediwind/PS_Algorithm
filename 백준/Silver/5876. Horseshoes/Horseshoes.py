def valid(string):
    # 길이가 홀수면 불가능
    if len(string) % 2 != 0:
        return False
    
    # 첫 번째 오른쪽 괄호의 위치 찾기
    first_right = -1
    for i in range(len(string)):
        if string[i] == ')':
            first_right = i
            break
    
    # 오른쪽 괄호가 없거나, 왼쪽 괄호가 없는 경우
    if first_right == -1 or first_right == 0:
        return False
    
    # 왼쪽 부분이 모두 '('인지 확인
    left_part = string[:first_right]
    if any(c != '(' for c in left_part):
        return False
    
    # 오른쪽 부분이 모두 ')'인지 확인
    right_part = string[first_right:]
    if any(c != ')' for c in right_part):
        return False
    
    # 왼쪽과 오른쪽 부분의 길이가 같은지 확인
    return len(left_part) == len(right_part)


def DFS(x, y):
    global ans
    
    ch[x][y] = 1
    res.append(board[x][y])
    
    if valid(res):
        ans = max(ans, len(res))
    
    for d in range(4):
        xx = x + dx[d]
        yy = y + dy[d]
        
        if xx < 0 or xx >= n or yy < 0 or yy >= n:
            continue
        
        if not ch[xx][yy]:
            DFS(xx, yy)
            ch[xx][yy] = 0
            res.pop()


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(input()) for _ in range(n)]
ch = [[0 for _ in range(n)] for _ in range(n)]

ans = 0
res = list()
DFS(0, 0)
print(ans)