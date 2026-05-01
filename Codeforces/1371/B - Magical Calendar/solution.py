import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, r = map(int, input().split())
    
    if n <= r:
        # k가 n-1일 때까지의 합 + (k >= n일 때의 일직선 모양 1개)
        ans = n * (n - 1) // 2 + 1
    else:
        # r이 n보다 작으므로 1부터 r까지의 합만 계산
        ans = r * (r + 1) // 2
        
    print(ans)