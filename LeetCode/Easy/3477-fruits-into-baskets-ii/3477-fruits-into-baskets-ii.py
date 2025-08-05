class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        ch = [0 for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if ch[j]:
                    continue
                if fruits[i] <= baskets[j]:
                    ch[j] = 1
                    break

        return sum(c == 0 for c in ch)
