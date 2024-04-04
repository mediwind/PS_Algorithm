class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = list()
        if nums == [0] * len(nums):
            answer = [0] * len(nums)
            return answer
        
        res = 1
        flag = False
        for num in nums:
            if num:
                res *= num
            if not num:
                flag = True
        
        for num in nums:
            if num:
                if flag:
                    answer.append(0)
                else:
                    answer.append(res//num)
            else:
                answer.append(res)
        
        return answer