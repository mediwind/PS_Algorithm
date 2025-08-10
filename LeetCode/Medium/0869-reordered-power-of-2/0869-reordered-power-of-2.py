class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power2_digits = set()
        x = 1
        while x <= 10**9:
            power2_digits.add(tuple(sorted(str(x))))
            x *= 2
            
        return tuple(sorted(str(n))) in power2_digits