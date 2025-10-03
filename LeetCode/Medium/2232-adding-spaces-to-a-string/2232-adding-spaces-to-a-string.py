class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        si = 0
        n = len(spaces)
        for i, ch in enumerate(s):
            if si < n and i == spaces[si]:
                res.append(' ')
                si += 1
            res.append(ch)
            
        return ''.join(res)