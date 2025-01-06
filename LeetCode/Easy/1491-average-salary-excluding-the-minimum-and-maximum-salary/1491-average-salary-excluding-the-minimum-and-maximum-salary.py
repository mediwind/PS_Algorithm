class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)

        mini = float("inf")
        maxi = float("-inf")

        ans = 0
        for s in salary:
            ans += s
            mini = min(mini, s)
            maxi = max(maxi, s)
        
        ans -= mini
        ans -= maxi

        return ans / (n - 2)
