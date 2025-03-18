class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        length = [1 for _ in range(n)] # LIS의 길이
        count = [1 for _ in range(n)] # LIS의 개수

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j] # 이는 nums[j]를 마지막 원소로 하는 LIS의 개수가 그대로 nums[i]를 마지막 원소로 하는 LIS의 개수가 된다는 것을 의미
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
        
        # print('length:', length)
        # print('count:', count)

        max_length = max(length)
        ans = 0
        for i in range(n):
            if length[i] == max_length:
                ans += count[i]
        return ans