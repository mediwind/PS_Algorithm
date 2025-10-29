class Solution:
    def smallestNumber(self, n: int) -> int:
        k = n.bit_length()
        if n == (1 << k) - 1:
            return n
            
        return (1 << k) - 1