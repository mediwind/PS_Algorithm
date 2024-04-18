from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        Q = deque(s)
        for i in t:
            if Q and Q[0] == i:
                Q.popleft()
        
        if Q:
            return False
        else:
            return True