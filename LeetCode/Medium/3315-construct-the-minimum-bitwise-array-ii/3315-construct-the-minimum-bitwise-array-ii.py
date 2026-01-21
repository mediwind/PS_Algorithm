class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = list()

        for num in nums:
            if num == 2:
                ans.append(-1)
                continue

            num_copy = num
            count = 0

            while num & 1 == 1:
                count += 1
                num >>= 1
            
            ans.append(num_copy - 2 ** (count-1))
        
        return ans