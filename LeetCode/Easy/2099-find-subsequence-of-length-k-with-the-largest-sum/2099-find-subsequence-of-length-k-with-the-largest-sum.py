class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = [(val, idx) for idx, val in enumerate(nums)]
        arr.sort(key = lambda x: -x[0])

        ans = list()
        for i in range(k):
            ans.append(arr[i])
        
        ans.sort(key = lambda x: x[1])
        ans = [x0 for x0, x1 in ans]
        return ans