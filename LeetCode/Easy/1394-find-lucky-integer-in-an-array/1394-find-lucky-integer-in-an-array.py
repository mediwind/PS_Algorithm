class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        ans = -1
        for key, val in count.items():
            if key == val:
                ans = max(ans, key)
        
        return ans