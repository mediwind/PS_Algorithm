class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        count = 0
        
        # 먼저 최대 OR 값을 구한다
        for mask in range(1, 1 << n):
            curr_or = 0
            for i in range(n):
                if mask & (1 << i):
                    curr_or |= nums[i]
            max_or = max(max_or, curr_or)
        
        # 다시 최대 OR 값을 만드는 부분집합의 개수를 센다
        for mask in range(1, 1 << n):
            curr_or = 0
            for i in range(n):
                if mask & (1 << i):
                    curr_or |= nums[i]
            if curr_or == max_or:
                count += 1
        
        return count