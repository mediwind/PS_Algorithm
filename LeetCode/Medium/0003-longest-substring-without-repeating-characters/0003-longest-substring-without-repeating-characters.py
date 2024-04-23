class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        lt, rt = 0, 0
        word = s[0]
        answer = 1
        while lt <= rt:
            if len(set(word)) != rt - lt + 1:
                lt += 1
                word = word[1:]
            else:
                answer = max(answer, len(word))
                rt += 1
                if rt <= n - 1:
                    word += s[rt]
        
        return answer