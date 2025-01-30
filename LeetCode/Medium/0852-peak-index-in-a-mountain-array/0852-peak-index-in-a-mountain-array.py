class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        lt, rt = 0, n - 1
        while lt < rt:
            mid = (lt + rt) // 2
            if arr[mid] > arr[mid + 1]:
                rt = mid
            else:
                lt = mid + 1
        
        return lt
