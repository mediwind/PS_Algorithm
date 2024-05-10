class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return list()
        
        ans = list()
        start = nums[0]
        cnt = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                if cnt > 0:
                    ans.append(f'{start}->{start + cnt}')
                else:
                    ans.append(str(start))
                start = nums[i]
                cnt = 0

        print(ans)
        print(start, cnt)

        if start == start + cnt: # that is cnt is 0
            ans.append(str(start))
        else:
            ans.append(f'{start}->{start + cnt}')

        return ans