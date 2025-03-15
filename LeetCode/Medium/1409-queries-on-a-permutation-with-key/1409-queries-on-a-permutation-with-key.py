class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))

        ans = list()
        for q in queries:
            pos = P.index(q)
            ans.append(pos)
            P.insert(0, P.pop(pos))
        
        return ans