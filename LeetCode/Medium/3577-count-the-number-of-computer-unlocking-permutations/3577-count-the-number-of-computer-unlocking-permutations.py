class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        head = complexity[0]

        for i in range(1, n):
            if complexity[i] <= head:
                return 0
        
        ans = 1
        for i in range(2, n):
            ans = (ans * i) % (10 ** 9 + 7)
        
        return ans