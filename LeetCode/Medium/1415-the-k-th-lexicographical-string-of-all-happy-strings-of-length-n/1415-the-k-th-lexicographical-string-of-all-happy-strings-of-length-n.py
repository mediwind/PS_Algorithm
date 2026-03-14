class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def DFS(prefix, n, k):
            if n == 0:
                return prefix

            for char in 'abc':
                if prefix and char == prefix[-1]:
                    continue

                cnt = 2 ** (n2 - len(prefix) - 1)

                if cnt >= k:
                    return DFS(prefix + char, n - 1, k)
                else:
                    k -= cnt

            return ""
        
        n2 = n
        return DFS("", n, k)