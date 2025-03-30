class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]
        
        for i in range(1, n + 1):
            for comb in itertools.combinations(nums, i):
                ans.append(list(comb))

        return ans