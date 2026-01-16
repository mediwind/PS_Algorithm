from functools import lru_cache
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

S = input().strip()
L = len(S)

@lru_cache(maxsize=None)
def dfs(idx, cnt, is_found, is_tight):
    if idx == L:
        return 1 if is_found else 0

    limit = int(S[idx]) if is_tight else 9
    
    count = 0
    
    for digit in range(limit + 1):
        next_tight = is_tight and (digit == limit)
        
        if is_found:
            count += dfs(idx + 1, 0, True, next_tight)
        else:
            if digit == 6:
                if cnt + 1 >= 3:
                    count += dfs(idx + 1, 3, True, next_tight)
                else:
                    count += dfs(idx + 1, cnt + 1, False, next_tight)
            else:
                count += dfs(idx + 1, 0, False, next_tight)
                
    return count

print(dfs(0, 0, False, True))