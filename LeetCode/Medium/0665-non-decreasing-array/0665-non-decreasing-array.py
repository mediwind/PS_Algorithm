class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 수정 횟수를 기록
        modified = 0
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # 이미 한 번 수정했으면 False 반환
                if modified == 1:
                    return False
                
                # 수정 필요
                modified += 1
                
                # nums[i]를 수정할지 nums[i+1]을 수정할지 결정
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]  # nums[i]를 낮춤
                else:
                    nums[i + 1] = nums[i]  # nums[i+1]을 높임
        
        return True