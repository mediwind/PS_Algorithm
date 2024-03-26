class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_cnt = dict()
        for num in nums:
            num_cnt[num] = num_cnt.get(num, 0) + 1
            if num_cnt[num] >= 2:
                num_cnt[num] = 2
        
        nums[:] = list()
        for k, v in num_cnt.items():
            nums += [k] * v
        k = len(nums)