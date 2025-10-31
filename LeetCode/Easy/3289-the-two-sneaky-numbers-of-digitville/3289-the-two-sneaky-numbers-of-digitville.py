class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []
        for x in nums:

            if x in seen:
                res.append(x)

                if len(res) == 2:
                    return res
            else:
                seen.add(x)
                
        return res