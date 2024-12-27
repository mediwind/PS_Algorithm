class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = list()
        ans = [0 for _ in range(n)]

        for idx, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                temp, order = stack.pop()
                ans[order] = idx - order
            stack.append((val, idx))
        
        return ans