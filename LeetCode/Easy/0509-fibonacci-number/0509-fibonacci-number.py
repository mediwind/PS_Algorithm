class Solution:
    def fib(self, n: int) -> int:
        dy = [0, 1]

        for i in range(2, n + 1):
            tmp = sum(dy[i - 2:i])
            dy.append(tmp)
        
        return dy[n]