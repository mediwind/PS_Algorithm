class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        idx = 0
        s_dict = dict()
        for i in s:
            if i not in s_dict:
                idx += 1
                s_dict[i] = idx
        
        idx = 0
        t_dict = dict()
        for i in t:
            if i not in t_dict:
                idx += 1
                t_dict[i] = idx
        
        snum, tnum = '', ''
        for i in range(n):
            snum += str(s_dict[s[i]])
            tnum += str(t_dict[t[i]])
        
        return snum == tnum