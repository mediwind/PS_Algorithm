class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()

        for cnt in range(len(nums) + 1):
            for comb in itertools.combinations(nums, cnt):
                answer.add(comb)
        
        return list(map(list, answer))