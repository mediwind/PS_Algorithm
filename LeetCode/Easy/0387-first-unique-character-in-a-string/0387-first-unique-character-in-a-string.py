class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for key in count:
            if count[key] == 1:
                return s.index(key)
        
        return -1