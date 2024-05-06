from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = list(map(sorted, strs))
        sorted_strs = list(map(''.join, sorted_strs))
        sorted_strs

        words = defaultdict(list)
        for idx, val in enumerate(sorted_strs):
            words[val].append(idx)

        ans = list()
        for val in words.values():
            tmp = list()
            for v in val:
                tmp.append(strs[v])
            ans.append(tmp)
        
        return ans