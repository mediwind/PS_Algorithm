class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def solve(n, k):
            if n == 1:
                return '0'
            
            mid = 1 << (n - 1)
            
            if k == mid:
                return '1'
            elif k < mid:
                return solve(n - 1, k)
            else:
                mirrored = (1 << n) - k
                bit = solve(n - 1, mirrored)
                return '1' if bit == '0' else '0'
        
        return solve(n, k)