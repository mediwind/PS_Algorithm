class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        

        def DFS(res):
            if len(res) == n:
                ans.append(res)
                return
            
            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    DFS(res + [key])
                    counter[key] += 1
        

        n = len(nums)
        counter = collections.Counter(nums)

        ans = list()
        res = list()

        DFS(res)
        return ans