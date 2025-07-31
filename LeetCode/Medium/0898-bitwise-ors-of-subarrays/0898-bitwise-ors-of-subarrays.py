class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        prev = set()

        for num in arr:
            cur = {num}
            for p in prev:
                cur.add(num | p)
            ans |= cur
            prev = cur
        
        return len(ans)