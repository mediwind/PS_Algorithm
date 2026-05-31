import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    # 1. 배치가 가능한 최대 룩의 개수를 넘어서면 불가능 (-1)
    if k > (n + 1) // 2:
        print(-1)
    else:
        # 2. 격자를 한 줄씩 만들면서 출력
        rooks_placed = 0
        for i in range(n):
            row = []
            for j in range(n):
                # 대각선 상에 위치하고, 홀수 번째 칸(인덱스로는 짝수)이며, 배치할 룩이 남은 경우
                if i == j and i % 2 == 0 and rooks_placed < k:
                    row.append('R')
                    rooks_placed += 1
                else:
                    row.append('.')
            print("".join(row))