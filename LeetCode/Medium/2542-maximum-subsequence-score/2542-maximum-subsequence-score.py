class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key = lambda x: x[1], reverse = True)

        minQ = list()
        n1Sum = 0
        res = 0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minQ, n1)

            if len(minQ) > k:
                n1Pop = heapq.heappop(minQ)
                n1Sum -= n1Pop
            if len(minQ) == k:
                res = max(res, n1Sum * n2)
        
        return res