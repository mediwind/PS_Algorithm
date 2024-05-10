class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return list()
        
        ans = list()
        start, end = nums[0], nums[0]
        for i in range(1, n):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(f'{start}->{end}')
                start, end = nums[i], nums[i]

        if start == end:
            ans.append(str(start))
        else:
            ans.append(f'{start}->{end}')

        return ans