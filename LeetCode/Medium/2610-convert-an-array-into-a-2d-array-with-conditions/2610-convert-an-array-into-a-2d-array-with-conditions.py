class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        count = collections.Counter(nums)

        ans = list()
        while n:
            arr = list()

            for key, val in count.items():
                if count[key]:
                    count[key] -= 1
                    arr.append(key)
                    n -= 1

            ans.append(arr)

        return ans