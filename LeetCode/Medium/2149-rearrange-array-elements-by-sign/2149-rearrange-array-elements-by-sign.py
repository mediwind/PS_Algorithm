class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        positive = list()
        negative = list()
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        ans = list()
        for i in range(n // 2):
            ans.append(positive[i])
            ans.append(negative[i])
        
        return ans