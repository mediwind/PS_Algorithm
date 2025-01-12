class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5: 0, 10: 0, 20: 0}

        for b in bills:
            if b == 5:
                changes[5] += 1
            elif b == 10:
                if changes[5] == 0:
                    return False
                changes[5] -= 1
                changes[10] += 1
            else:
                if changes[10] >= 1 and changes[5] >= 1:
                    changes[10] -= 1
                    changes[5] -= 1
                    changes[20] += 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                    changes[20] += 1
                else:
                    return False
        
        return True