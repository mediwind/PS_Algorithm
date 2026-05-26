import sys
import math
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    k = int(input())
    
    m = math.ceil(math.sqrt(k))
    
    start = (m - 1) ** 2 + 1
    corner = start + m - 1
    
    if k < corner:
        # 모퉁이에 도달하기 전 (위에서 아래로 내려오는 중)
        row = k - start + 1
        col = m
    elif k == corner:
        # 정확히 모퉁이 지점
        row = m
        col = m
    else:
        # 모퉁이를 지나친 후 (오른쪽에서 왼쪽으로 가는 중)
        row = m
        col = m * m - k + 1
        
    print(row, col)