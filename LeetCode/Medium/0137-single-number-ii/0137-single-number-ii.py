class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        
        for x in nums:
            cnt[x] += 1

        for x, freq in cnt.items():
            if freq == 1:
                return x
        
        return -1