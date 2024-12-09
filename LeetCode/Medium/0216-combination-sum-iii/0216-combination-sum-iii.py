class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def DFS(L, start, num):
            nonlocal ans
            if L == k:
                if num == n:
                    ans.append(res[:])
                return
            
            for i in range(start, 10):
                res.append(i)
                DFS(L + 1, i + 1, num + i)
                res.pop()
        
        ans = list()
        res = list()
        DFS(0, 1, 0)
        return ans
