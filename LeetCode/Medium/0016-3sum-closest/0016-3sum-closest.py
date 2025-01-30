class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            lt, rt = i + 1, len(nums) - 1
            
            while lt < rt:
                current_sum = nums[i] + nums[lt] + nums[rt]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    lt += 1
                elif current_sum > target:
                    rt -= 1
                else:
                    return current_sum
        
        return closest_sum