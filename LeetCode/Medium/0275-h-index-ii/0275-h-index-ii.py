class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        lt, rt = 0, n - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if citations[mid] + mid >= n:
                rt = mid - 1
            else:
                lt = mid + 1
        return n - lt