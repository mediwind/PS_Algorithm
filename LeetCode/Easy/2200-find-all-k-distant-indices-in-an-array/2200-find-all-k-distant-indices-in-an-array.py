class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        mark = [False for _ in range(n)]
        for idx, val in enumerate(nums):
            if val == key:
                left = max(0, idx - k)
                right = min(n - 1, idx + k)
                for i in range(left, right + 1):
                    mark[i] = True
                    
        return [i for i, v in enumerate(mark) if v]