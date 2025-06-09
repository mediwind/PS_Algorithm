import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def is_makeable(n, allowed):
    # n의 각 자리수가 allowed에 있는지 확인
    while n:
        if not allowed[n % 10]:
            return False
        n //= 10
    return True


def min_multiplications(n, allowed, memo):
    if n in memo:
        return memo[n]
    
    if is_makeable(n, allowed):
        memo[n] = 0
        return 0
    
    res = float('inf')
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_makeable(i, allowed):
            sub = min_multiplications(n // i, allowed, memo)
            if sub != float('inf'):
                res = min(res, sub + 1)
    memo[n] = res
    
    return res


T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    N, cards = arr[0], arr[1:]
    
    allowed = [False for _ in range(10)]
    for c in cards:
        allowed[c] = True
        
    Q = int(input())
    for _ in range(Q):
        K = int(input())
        memo = dict()
        ans = min_multiplications(K, allowed, memo)
        print(ans if ans != float('inf') else -1)