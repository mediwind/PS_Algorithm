class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        tmp = arr[1] - arr[0]
        for i in range(2, n):
            if tmp != arr[i] - arr[i - 1]:
                return False
            tmp = arr[i] - arr[i - 1]
        return True