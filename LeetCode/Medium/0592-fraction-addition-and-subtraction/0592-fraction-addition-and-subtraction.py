import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        import math
        i, n = 0, len(expression)
        num_sum, den_sum = 0, 1
        while i < n:
            sign = 1
            if expression[i] in '+-':
                sign = 1 if expression[i] == '+' else -1
                i += 1
            j = i
            while expression[j].isdigit():
                j += 1
            num = int(expression[i:j]) * sign
            i = j + 1
            j = i
            
            while j < n and expression[j].isdigit():
                j += 1
            den = int(expression[i:j])
            i = j
            g = math.gcd(den_sum, den)
            lcm = den_sum // g * den
            num_sum = num_sum * (lcm // den_sum) + num * (lcm // den)
            den_sum = lcm

            if num_sum == 0:
                den_sum = 1
            else:
                gg = math.gcd(abs(num_sum), den_sum)
                num_sum //= gg
                den_sum //= gg

        return f"{num_sum}/{den_sum}"