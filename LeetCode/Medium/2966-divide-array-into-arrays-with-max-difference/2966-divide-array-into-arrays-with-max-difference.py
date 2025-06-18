class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        ans = []
        for i in range(0, len(nums), 3):
            tmp = nums[i:i + 3]
            if tmp[-1] - tmp[0] > k:
                    return []
            ans.append(tmp)
        
        return ans
