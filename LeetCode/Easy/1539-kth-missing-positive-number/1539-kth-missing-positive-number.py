class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lt, rt = 0, len(arr) - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                lt = mid + 1
            else:
                rt = mid - 1
        
        return lt + k