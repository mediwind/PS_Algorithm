class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        standard = math.floor(len(nums) / 3)

        ans = set()
        for key, val in counter.items():
            if val > standard and key not in ans:
                ans.add(key)
        
        return sorted(list(ans))