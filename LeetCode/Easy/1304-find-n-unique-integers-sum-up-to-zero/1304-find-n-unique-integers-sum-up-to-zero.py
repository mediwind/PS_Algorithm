class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = list()

        for i in range(-(n // 2), n // 2 + 1):
            if i == 0 and n % 2 == 0:
                continue
            ans.append(i)
        
        return ans
