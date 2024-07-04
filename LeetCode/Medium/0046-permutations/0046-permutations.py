class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def DFS(L):
            if L == n:
                answer.append(res[:])
                return

            for i in range(n):
                if not ch[i]:
                    ch[i] = 1
                    res[L] = nums[i]
                    DFS(L + 1)
                    ch[i] = 0

        n = len(nums)
        ch = [0 for _ in range(n)]
        res = [0 for _ in range(n)]
        answer = list()
        DFS(0)

        return answer