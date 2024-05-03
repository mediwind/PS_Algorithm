class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        s = s.split()

        if n != len(s):
            return False

        p_dict = dict()
        s_dict = dict()
        for i in range(n):
            if pattern[i] in p_dict and p_dict[pattern[i]] != s[i]:
                return False
            p_dict[pattern[i]] = s[i]
            if s[i] in s_dict and s_dict[s[i]] != pattern[i]:
                return False
            s_dict[s[i]] = pattern[i]
    
        return True