class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev = 0
        streek = 1

        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                streek += 1
            else:
                prev = streek
                streek = 1

            if streek <= prev:
                ans += 1

        return ans