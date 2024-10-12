class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # left_product와 right_product는 각각 *_product[i] 바로 왼쪽 직전과 오른쪽 직전까지의 누적곱을 의미
        left_product = [1 for _ in range(n)]
        right_product = [1 for _ in range(n)]
        answer = list()

        for i in range(1, n):
            left_product[i] = nums[i - 1] * left_product[i - 1]
        
        for i in range(n - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]
        
        for i in range(n):
            tmp = left_product[i] * right_product[i]
            answer.append(tmp)
        
        return answer