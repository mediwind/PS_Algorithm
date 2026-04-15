class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = n
        for i, w in enumerate(words):
            if w == target:
                t = abs(i - startIndex)
                ans = min(ans, t, n - t)

        if ans == n:
            return -1
        return ans