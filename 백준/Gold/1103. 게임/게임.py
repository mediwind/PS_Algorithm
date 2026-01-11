import sys

# 재귀 깊이 제한 해제 (DFS 깊이가 깊어질 수 있음)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve():
    # N, M 입력 (1 ~ 50)
    # 문자열로 들어오는 입력을 처리하기 위해 strip() 사용
    line1 = input().split()
    if not line1: return
    N, M = map(int, line1)
    
    board = []
    for _ in range(N):
        # 'H'가 아닌 숫자는 정수형으로 변환하지 않고 문자로 둠 (H 처리 편의상)
        # 나중에 계산할 때만 int() 변환
        board.append(list(input().strip()))
        
    # dp[r][c]: (r, c)에서 출발했을 때 가능한 최대 이동 횟수
    # 방문하지 않은 곳은 -1로 초기화
    dp = [[-1] * M for _ in range(N)]
    
    # visited[r][c]: 현재 탐색 경로(스택)에 포함되어 있는지 여부 (사이클 판별용)
    visited = [[False] * M for _ in range(N)]
    
    # 방향 벡터 (상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def dfs(r, c):
        # 1. 범위를 벗어나거나 구멍(H)에 빠지면 게임 종료 -> 이동 횟수 0 반환
        if r < 0 or r >= N or c < 0 or c >= M or board[r][c] == 'H':
            return 0
        
        # 2. 사이클 판별: 현재 방문 중인 경로를 다시 밟았다면 무한 루프
        if visited[r][c]:
            print(-1)
            sys.exit() # 프로그램 즉시 종료
            
        # 3. 메모이제이션: 이미 계산해둔 값이 있다면 바로 반환
        if dp[r][c] != -1:
            return dp[r][c]
        
        # 4. 탐색 시작
        visited[r][c] = True # 현재 경로에 추가
        
        current_val = int(board[r][c]) # 현재 칸의 숫자 X
        max_moves = 0
        
        for i in range(4):
            nr = r + (dr[i] * current_val)
            nc = c + (dc[i] * current_val)
            
            # 다음 칸에서의 최대 이동 횟수를 재귀적으로 구함
            # 현재 칸 이동(1) + 다음 칸에서의 최대값
            max_moves = max(max_moves, dfs(nr, nc) + 1)
            
        visited[r][c] = False # 백트래킹 (경로에서 빠져나옴)
        
        # 5. 결과 저장 및 반환
        dp[r][c] = max_moves
        return max_moves

    # 시작점 (0,0)에서 탐색 시작
    # (0,0)도 첫 이동에 포함되므로 dfs 결과가 바로 답
    # 단, 문제 정의상 '움직이는 횟수'를 구하라고 했으나, 
    # 보통 이런 문제는 '방문한 칸의 수'인지 '간선의 수'인지 헷갈림.
    # 로직상: 
    # - 구멍/범위밖 도달 시 return 0
    # - 한 칸 움직일 때마다 +1 해서 돌아옴
    # 따라서 dfs(0,0)은 (0,0)을 밟은 상태에서 출발하므로 논리적으로 맞음.
    print(dfs(0, 0))

solve()