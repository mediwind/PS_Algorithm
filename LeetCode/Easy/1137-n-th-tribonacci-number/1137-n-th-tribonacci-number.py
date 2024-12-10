class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        arr += [0 for _ in range(35)]
        for i in range(3, 38):
            arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1]
        
        return arr[n]