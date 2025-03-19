class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])

        current_end = float('-inf')
        ans = 0
        for start, end in pairs:
            if start > current_end:
                current_end = end
                ans += 1
        
        return ans