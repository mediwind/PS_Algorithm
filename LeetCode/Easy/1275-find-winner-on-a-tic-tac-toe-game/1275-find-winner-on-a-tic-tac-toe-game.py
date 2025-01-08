class Solution:
    def check_winner(self, board, player):
        # Check rows and columns
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
            return True
        return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        n = len(moves)
        board = [[0 for _ in range(3)] for _ in range(3)]

        for i in range(n):
            x, y = moves[i]
            if i % 2 == 0:
                board[x][y] = 'A'
            else:
                board[x][y] = 'B'

        # Check if player A or B has won
        if self.check_winner(board, 'A'):
            return "A"
        if self.check_winner(board, 'B'):
            return "B"

        # Check if the game is still pending or a draw
        if n == 9:
            return "Draw"
        else:
            return "Pending"