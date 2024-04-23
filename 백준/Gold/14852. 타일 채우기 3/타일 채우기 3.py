MOD = 1_000_000_007

def tile_filling(n):
    dy = [0] * (n + 2)
    dy[0] = 1
    dy[1] = 2
    dy[2] = 7
    if n <= 2:
        return dy[n]
    
    for i in range(3, n+1):
        dy[i] = (3*dy[i-1] + dy[i-2] - dy[i-3]) % MOD
    
    return dy[n]

n = int(input())
print(tile_filling(n))