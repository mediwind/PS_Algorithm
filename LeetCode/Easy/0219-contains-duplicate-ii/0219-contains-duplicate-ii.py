from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        indices = defaultdict(list)
        for i in range(n):
            indices[nums[i]].append(i)
        
        for key, val in indices.items():
            if len(val) >= 2:
                for i in range(len(val) - 1):
                    if abs(val[i] - val[i + 1]) <= k:
                        return True
        
        return False