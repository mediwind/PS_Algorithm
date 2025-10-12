class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        cur = []
        for ch in target:
            cur.append('a')
            res.append(''.join(cur))
            steps = ord(ch) - ord('a')
            for _ in range(steps):
                cur[-1] = chr((ord(cur[-1]) - ord('a') + 1) % 26 + ord('a'))
                res.append(''.join(cur))
                
        return res