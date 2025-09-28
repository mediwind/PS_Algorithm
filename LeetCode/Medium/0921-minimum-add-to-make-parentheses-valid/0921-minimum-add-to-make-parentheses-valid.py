class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = 0
        open_count = 0
        for ch in s:
            if ch == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    need += 1
                    
        return need + open_count