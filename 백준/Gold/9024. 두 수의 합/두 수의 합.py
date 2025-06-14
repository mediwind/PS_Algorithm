import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort()
    
    min_diff = float('inf')
    for i in range(N):
        lt, rt = i + 1, N - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            res = arr[i] + arr[mid]
            
            if res > K:
                rt = mid - 1
            else:
                lt = mid + 1
            
            if abs(K - res) < min_diff:
                ans = 1
                min_diff = abs(K - res)
            elif abs(K - res) == min_diff:
                ans += 1
    
    print(ans)