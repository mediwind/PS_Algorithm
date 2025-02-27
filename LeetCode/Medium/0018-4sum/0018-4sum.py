class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 배열 정렬
        nums.sort()
        n = len(nums)
        result = list()
        
        # 첫 번째 숫자 선택
        for i in range(n - 3):
            # i에 대한 중복 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 두 번째 숫자 선택
            for j in range(i + 1, n - 2):
                # j에 대한 중복 건너뛰기
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # 나머지 두 숫자는 투 포인터로 찾기
                left = j + 1
                right = n - 1
                
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # left 포인터의 중복 건너뛰기
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # right 포인터의 중복 건너뛰기
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result