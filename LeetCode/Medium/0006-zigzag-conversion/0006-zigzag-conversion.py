class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        board = ['' for _ in range(numRows)]
        answer = ''

        i = 0
        to_down = True

        for x in s:
            board[i] += x
            if i == 0:
                to_down = True
            elif i == numRows - 1:
                to_down = False
            
            if to_down:
                i += 1
            else:
                i -= 1
        
        for i in range(numRows):
            answer += board[i]
        
        return answer