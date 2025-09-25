class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a = sorted(s1)
        b = sorted(s2)

        ge = all(x >= y for x, y in zip(a, b))
        le = all(x <= y for x, y in zip(a, b))
        
        return ge or le