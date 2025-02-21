def print_board(board):
    for row in board:
        print(" ".join(cell if cell is not None else '.' for cell in row))
    print()

def insert_left(board, row, marker):
    n = len(board)
    # 행의 왼쪽에서부터 빈 칸 찾기
    pos = None
    for j in range(n):
        if board[row][j] is None:
            pos = j
            break
    if pos is None:
        # 빈 칸이 없으면, 마지막 칸은 밀려나게 됨.
        pos = n - 1
    # 오른쪽부터 pos까지 한 칸씩 밀기
    for j in range(pos, 0, -1):
        board[row][j] = board[row][j-1]
    board[row][0] = marker

def insert_right(board, row, marker):
    n = len(board)
    pos = None
    for j in range(n-1, -1, -1):
        if board[row][j] is None:
            pos = j
            break
    if pos is None:
        pos = 0
    # 왼쪽부터 pos까지 한 칸씩 밀기
    for j in range(pos, n-1):
        board[row][j] = board[row][j+1]
    board[row][n-1] = marker

def insert_top(board, col, marker):
    n = len(board)
    pos = None
    for i in range(n):
        if board[i][col] is None:
            pos = i
            break
    if pos is None:
        pos = n - 1
    # 아래로 밀기
    for i in range(pos, 0, -1):
        board[i][col] = board[i-1][col]
    board[0][col] = marker

def insert_bottom(board, col, marker):
    n = len(board)
    pos = None
    for i in range(n-1, -1, -1):
        if board[i][col] is None:
            pos = i
            break
    if pos is None:
        pos = 0
    # 위로 밀기
    for i in range(pos, n-1):
        board[i][col] = board[i+1][col]
    board[n-1][col] = marker

def count_straights(board, marker):
    n = len(board)
    straight_count = 0
    # 행 검증
    for i in range(n):
        if all(board[i][j] == marker for j in range(n)):
            straight_count += 1
    # 열 검증
    for j in range(n):
        if all(board[i][j] == marker for i in range(n)):
            straight_count += 1
    return straight_count

def game_winner(board):
    xs = count_straights(board, 'X')
    os = count_straights(board, 'O')
    if xs > os:
        return "X WINS"
    elif os > xs:
        return "O WINS"
    else:
        return None

def main():
    import sys
    input = sys.stdin.readline
    N_line = input().strip()
    if not N_line:
        return
    N = int(N_line)
    # 초기 보드 생성 (None으로 빈 칸을 표시)
    board = [[None] * N for _ in range(N)]
    
    turn = 0  # 0: X, 1: O; X가 먼저 시작
    # moves를 한 줄씩 읽으면서 처리
    while True:
        line = input().strip()
        if not line:
            continue
        if line == "QUIT":
            print("TIE GAME")
            break
        
        # 현재 턴의 플레이어 결정
        marker = 'X' if turn % 2 == 0 else 'O'
        
        # move의 형식: 'L2','R3','T1','B4'와 같이 구성, 숫자는 1-indexed
        direction = line[0]
        idx = int(line[1:]) - 1  # 0-indexed
        if direction == 'L':
            insert_left(board, idx, marker)
        elif direction == 'R':
            insert_right(board, idx, marker)
        elif direction == 'T':
            insert_top(board, idx, marker)
        elif direction == 'B':
            insert_bottom(board, idx, marker)
        
        # (디버그용) 보드 출력
        # print_board(board)
        
        # 승리 조건 검사
        result = game_winner(board)
        if result is not None:
            print(result)
            break
        
        # 턴 전환
        turn += 1

if __name__ == '__main__':
    main()