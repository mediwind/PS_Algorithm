class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = set()
        common_count = 0
        ans = list()
        for i in range(n):
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])
            
            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])
            
            ans.append(common_count)
            
        return ans