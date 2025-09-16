class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        from math import gcd

        stack = list()
        for x in nums:
            cur = x
            while stack:
                a = stack[-1]
                g = gcd(a, cur)
                if g == 1:
                    break
                stack.pop()
                cur = (a // g) * cur
            stack.append(cur)

        return stack