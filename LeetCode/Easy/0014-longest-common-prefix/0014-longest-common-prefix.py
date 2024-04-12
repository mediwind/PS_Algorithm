class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        strs.sort(key = lambda x: (len(x), x))
        
        answer = ""
        for i in range(len(strs[0])):
            for j in range(1, n):
                if strs[0][i] != strs[j][i]:
                    return answer
            answer += strs[0][i]
        
        return answer