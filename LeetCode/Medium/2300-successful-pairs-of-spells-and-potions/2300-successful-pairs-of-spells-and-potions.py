class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)

        potions.sort()

        answer = list()
        for spell in spells:
            lt, rt = 0, len(potions) - 1
            while lt <= rt:
                mid = (lt + rt) // 2
                product = spell * potions[mid]
                
                if product >= success:
                    rt = mid - 1
                else:
                    lt = mid + 1
            
            res = m - lt
            answer.append(res)
        
        return answer