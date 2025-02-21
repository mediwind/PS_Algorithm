class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def DFS(total, start):
            nonlocal n

            if total > target:
                return
            
            if total == target:
                tmp = tuple(sorted(res))

                if not tmp in ans:
                    ans.append(tmp)

                return

            for i in range(start, n):
                num = candidates[i]

                if i > start and num == candidates[i - 1]:
                    continue

                res.append(num)
                DFS(total + num, i + 1)
                res.pop()
        
        candidates.sort()

        n = len(candidates)

        ans = list()
        res = list()
        DFS(0, 0)

        return ans