class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dy = [0 for _ in range(len(text1))]
        longest = 0

        for c in text2:
            cur_length = 0
            for i, val in enumerate(dy):
                if cur_length < val:
                    cur_length = val
                elif c == text1[i]:
                    dy[i] = cur_length + 1
                    longest = max(longest, cur_length + 1)
        
        return longest