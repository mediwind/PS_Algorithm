class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        prefix = [[0]*26 for _ in range(n+1)]
        for i,ch in enumerate(s):
            idx = ord(ch) - 97
            for c in range(26):
                prefix[i+1][c] = prefix[i][c]
            prefix[i+1][idx] += 1

        first = [-1]*26
        last = [-1]*26
        for i,ch in enumerate(s):
            idx = ord(ch)-97
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        ans = 0
        for c in range(26):
            if first[c] != -1 and first[c] < last[c]:
                l = first[c] + 1
                r = last[c]
                distinct = 0
                for k in range(26):
                    if prefix[r][k] - prefix[l][k] > 0:
                        distinct += 1
                ans += distinct

        return ans