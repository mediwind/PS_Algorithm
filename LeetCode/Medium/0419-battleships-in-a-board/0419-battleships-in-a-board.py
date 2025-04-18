class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        
        # 보드를 순회하며 배틀쉽의 시작점을 찾음
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 현재 위치가 'X'이고, 위쪽과 왼쪽이 배틀쉽이 아닌 경우에만 카운트
                if board[i][j] == 'X':
                    if (i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X'):
                        count += 1
        
        return count