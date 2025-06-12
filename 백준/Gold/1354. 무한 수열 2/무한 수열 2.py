import sys
sys.setrecursionlimit(10 ** 6)


def DFS(n):
    if n <= 0:
        return 1
    
    if n in memo:
        return memo[n]
    
    res = DFS(n // P - X) + DFS(n // Q - Y)
    memo[n] = res
    return res

N, P, Q, X, Y = map(int, input().split())
memo = {}

ans = DFS(N)
print(ans)