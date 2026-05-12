import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    # 1. 1부터 n까지의 배열을 한 번에 생성
    ans = list(range(1, n + 1))
    
    # 2. 짝수는 끝까지, 홀수는 마지막 3개 전까지 인접한 원소 스왑
    limit = n if n % 2 == 0 else n - 3
    for i in range(0, limit, 2):
        ans[i], ans[i+1] = ans[i+1], ans[i]
        
    # 3. 홀수일 때 남은 꼬리 3개 처리 (파이썬의 다중 할당 활용)
    if n % 2 != 0:
        ans[-3], ans[-2], ans[-1] = ans[-2], ans[-1], ans[-3]
        
    print(*ans)