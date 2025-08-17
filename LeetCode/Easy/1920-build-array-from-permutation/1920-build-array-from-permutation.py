class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # 각 위치 i에 대해 nums[nums[i]]를 구해서 새 배열에 저장
        return [nums[nums[i]] for i in range(len(nums))]