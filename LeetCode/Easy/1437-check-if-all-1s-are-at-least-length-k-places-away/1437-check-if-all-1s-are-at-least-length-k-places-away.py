class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        check = list()
        for idx, val in enumerate(nums):
            if val == 1:
                check.append(idx)
        
        for i in range(1, len(check)):
            if check[i] - check[i - 1] - 1< k:
                return False
        
        return True