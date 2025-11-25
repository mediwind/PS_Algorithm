class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        from collections import defaultdict

        logs.sort(key = lambda x: (x[0], x[1]))
        count = defaultdict(set)
        for user, time in logs:
            count[user].add(time)
        
        ans = [0] * k
        for val in count.values():
            ans[len(val) - 1] += 1

        return ans