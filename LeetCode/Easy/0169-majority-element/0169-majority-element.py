class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        num_dict = dict()
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        
        for idx, val in num_dict.items():
            if num_dict[num] >= n//2 + 1:
                return num
