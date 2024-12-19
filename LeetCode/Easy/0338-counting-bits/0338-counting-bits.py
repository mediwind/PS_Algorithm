class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = list()
        for i in range(n + 1):
            res = bin(i)[2:].count('1')
            ans.append(res)
        return ans