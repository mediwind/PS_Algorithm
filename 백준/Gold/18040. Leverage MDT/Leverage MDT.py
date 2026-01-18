import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    grid = []
    for _ in range(N):
        grid.append(input().strip())

    if N == 0 or M == 0:
        print(0)
        return

    dp = [[0] * (M - 1) for _ in range(N)]
    
    max_side = 1

    for i in range(N):
        for j in range(M - 1):
            if grid[i][j] == grid[i][j+1]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                k = dp[i][j]
                
                current_max = k
                
                if i > 0 and dp[i-1][j] >= k:
                    current_max = k + 1
                
                max_side = max(max_side, current_max)
            else:
                pass

    print(max_side * max_side)

if __name__ == "__main__":
    solve()