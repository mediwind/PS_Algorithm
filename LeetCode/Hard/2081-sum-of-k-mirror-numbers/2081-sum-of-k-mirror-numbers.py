class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def to_base_k(x, k):
            res = list()
            while x:
                res.append(str(x % k))
                x //= k
            return ''.join(res[::-1]) if res else '0'

        ans = list()
        length = 1
        while len(ans) < n:

            # 홀수 길이 팰린드롬
            for half in range(10**(length-1), 10**length):
                s = str(half)
                pal = int(s + s[-2::-1])
                if str(pal) == str(pal)[::-1]:
                    basek = to_base_k(pal, k)
                    if basek == basek[::-1]:
                        ans.append(pal)
                        if len(ans) == n:
                            return sum(ans)

            # 짝수 길이 팰린드롬
            for half in range(10**(length-1), 10**length):
                s = str(half)
                pal = int(s + s[::-1])
                if str(pal) == str(pal)[::-1]:
                    basek = to_base_k(pal, k)
                    if basek == basek[::-1]:
                        ans.append(pal)
                        if len(ans) == n:
                            return sum(ans)

            length += 1
            
        return sum(ans)