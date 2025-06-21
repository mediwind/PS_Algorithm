class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).values())

        ans = float('inf')
        for target in freq:
            deletion_cnt = 0
            for f in freq:
                if f < target:
                    deletion_cnt += f
                elif f > target + k:
                    deletion_cnt += f - (target + k)
            
            ans = min(ans, deletion_cnt)
        
        return ans