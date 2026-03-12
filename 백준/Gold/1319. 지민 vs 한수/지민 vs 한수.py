import sys
input = sys.stdin.readline

N = int(input().strip())
trees = []
for _ in range(N):
    x, y, v = map(int, input().strip().split())
    trees.append((x, y, v))

min_diff = float('inf')

# 1. 두 개의 나무를 골라 기준선을 만듭니다.
for i in range(N):
    for j in range(i + 1, N):
        x1, y1, _ = trees[i]
        x2, y2, _ = trees[j]
        
        dx = x2 - x1
        dy = y2 - y1
        
        left_sum = 0
        right_sum = 0
        collinear = []
        
        # 2. 나머지 모든 나무들이 선의 어느 쪽에 있는지 판별합니다.
        for k in range(N):
            x3, y3, v3 = trees[k]
            
            # 외적 (Cross Product) 계산
            cross = dx * (y3 - y1) - dy * (x3 - x1)
            
            if cross > 0:
                left_sum += v3
            elif cross < 0:
                right_sum += v3
            else:
                collinear.append((x3, y3, v3))
                
        # 3. 선 위에 있는 나무들을 기하학적 순서(x좌표, y좌표 순)로 정렬합니다.
        collinear.sort(key=lambda item: (item[0], item[1]))
        
        # 4. 미세한 회전을 통해 선 위의 나무들을 양쪽으로 분할하는 모든 경우의 수를 탐색합니다.
        K = len(collinear)
        for split in range(K + 1):
            # split 인덱스를 기준으로 앞부분과 뒷부분의 가치 합 계산
            group1_sum = sum(v for _, _, v in collinear[:split])
            group2_sum = sum(v for _, _, v in collinear[split:])
            
            # 경우 1: 앞부분이 왼쪽 밭으로, 뒷부분이 오른쪽 밭으로 떨어지는 경우
            diff1 = abs((left_sum + group1_sum) - (right_sum + group2_sum))
            min_diff = min(min_diff, diff1)
            
            # 경우 2: 앞부분이 오른쪽 밭으로, 뒷부분이 왼쪽 밭으로 떨어지는 경우
            diff2 = abs((left_sum + group2_sum) - (right_sum + group1_sum))
            min_diff = min(min_diff, diff2)

print(min_diff)