class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums] #turns nums into max heap

        heapq.heapify(nums)

        for _ in range(k):
            min = heapq.heappop(nums)

        return -min