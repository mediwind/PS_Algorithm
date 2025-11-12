from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones

        g = 0
        for v in nums:
            g = gcd(g, v)
            
        if g != 1:
            return -1

        min_len = n + 1
        for i in range(n):
            cur = nums[i]
            if cur == 1:
                min_len = 1
                break
            for j in range(i + 1, n):
                cur = gcd(cur, nums[j])
                if cur == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return (min_len - 1) + (n - 1)