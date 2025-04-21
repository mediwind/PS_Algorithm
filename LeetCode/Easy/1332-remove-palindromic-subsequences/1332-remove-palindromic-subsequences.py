class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        
        # 문자열이 이미 회문인 경우 1단계
        if s == s[::-1]:
            return 1
        
        # 회문이 아닌 경우, 'a'와 'b'를 각각 제거해야 하므로 2단계
        return 2