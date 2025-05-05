class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter = dict()
        ans = 0

        for num1 in nums1:
            for num2 in nums2:
                tmp = num1 + num2
                counter[tmp] = counter.get(tmp, 0) + 1
        
        for num3 in nums3:
            for num4 in nums4:
                tmp = num3 + num4
                ans += counter.get(-tmp, 0)
        
        return ans
