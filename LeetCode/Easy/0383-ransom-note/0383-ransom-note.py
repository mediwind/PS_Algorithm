class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_dict = dict()
        for r in ransomNote:
            rn_dict[r] = rn_dict.get(r, 0) + 1

        for m in magazine:
            if m not in rn_dict:
                continue
            rn_dict[m] -= 1
        
        for val in rn_dict.values():
            if val > 0:
                return False
        
        return True