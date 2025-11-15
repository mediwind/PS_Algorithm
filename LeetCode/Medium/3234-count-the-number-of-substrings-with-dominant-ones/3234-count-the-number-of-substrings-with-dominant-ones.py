class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        
        Z = [-1] + [i for i, ch in enumerate(s) if ch == '0'] + [n]
        m = len(Z) - 2  

        
        def count_pairs_le(L: int, R: int, T: int) -> int:
            if T < 0 or L <= 0 or R <= 0:
                return 0
            
            if T >= L + R - 2:
                return L * R
            
            if L > R:
                L, R = R, L
            
            
            full = max(0, min(L, T - R + 2))
            
            a3 = full
            a4 = min(L - 1, T)
            rem = 0
            if a3 <= a4:
                cnt = a4 - a3 + 1
                
                rem = cnt * (T + 1) - (a3 + a4) * cnt // 2
            return full * R + rem

        
        dominant = 0
        import math
        B = int(math.isqrt(n))  
        for k in range(1, B + 1):
            need_sq = k * k
            
            for i in range(1, m - k + 2):
                left_gap = Z[i] - Z[i - 1]           
                right_gap = Z[i + k] - Z[i + k - 1]  
                base_len = Z[i + k - 1] - Z[i] + 1
                ones_inside = base_len - k
                
                
                T = need_sq - ones_inside
                
                bad = count_pairs_le(left_gap, right_gap, T - 1)
                total_pairs = left_gap * right_gap
                dominant += total_pairs - bad

        
        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            j = i
            while j < n and s[j] == '1':
                j += 1
            length = j - i
            dominant += length * (length + 1) // 2
            i = j

        return dominant