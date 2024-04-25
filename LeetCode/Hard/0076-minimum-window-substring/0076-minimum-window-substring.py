from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window = dict()

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        lt = 0
        for rt in range(len(s)):
            c = s[rt]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if rt - lt + 1 < resLen:
                    res = [lt, rt]
                    resLen = rt - lt + 1
                
                window[s[lt]] -= 1
                if s[lt] in countT and window[s[lt]] < countT[s[lt]]:
                    have -= 1
                
                lt += 1
        
        lt, rt = res

        if resLen != float('inf'):
            return s[lt:rt + 1]
        return ""