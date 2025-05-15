class Solution:
    def numDecodings(self, s: str) -> int:
        # 예외 처리: 빈 문자열 또는 첫 문자가 '0'인 경우
        if not s or s[0] == '0':
            return 0
        
        # dy[i]는 문자열 s의 처음 i개의 문자를 해독할 수 있는 방법의 수
        n = len(s)
        dy = [0 for _ in range(n + 1)]
        dy[0] = 1  # 빈 문자열을 해독하는 방법
        dy[1] = 1  # 첫 문자가 유효한 경우
        
        for i in range(2, n + 1):
            # 한 자리 숫자를 해독할 수 있는 경우
            if s[i - 1] != '0':
                dy[i] += dy[i - 1]
            
            # 두 자리 숫자를 해독할 수 있는 경우
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dy[i] += dy[i - 2]
        
        return dy[n]