class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = list()
        bigger = list()

        cnt = 0
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                cnt += 1
            else:
                bigger.append(num)
        
        ans = smaller + [pivot for _ in range(cnt)] + bigger
        return ans