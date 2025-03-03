class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        lt, rt = 0, (n - 1) - k
        while lt <= rt:
            mid = (lt + rt) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lt = mid + 1
            else:
                rt = mid - 1
        
        return arr[lt:lt + k]