class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        start = strs[0]
        end = strs[-1]
        answer = ""
        for i in range(min(len(start), len(end))):
            if start[i] != end[i]:
                return answer
            answer += start[i]
        
        return answer