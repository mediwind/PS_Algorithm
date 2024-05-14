def partitioning(x_line):
    # left, right는 수직선인 x_line보다 왼쪽, 오른쪽에 있는 소들
    left = [c for c in by_y if c[0] < x_line]
    right = [c for c in by_y if c[0] > x_line]
    
    res = float('inf')
    # 현재의 y 좌표 즉, 수평선인 y_line을 기준으로 left와 right에서 y_line 아래인 소들의 수
    left_at = 0
    right_at = 0
    while left_at + right_at < len(by_y):
        # left_at + right_at는 현재 y 좌표 아래에 있는 소들의 총 수를 나타냅니다.
        y_line = by_y[left_at + right_at][1] + 1
        
        # y_line보다 아래에 있는 left 소들의 수를 증가시킴
        while left_at < len(left) and y_line > left[left_at][1]:
            left_at += 1
        
        # y_line보다 아래에 있는 right 소들의 수를 증가시킴
        while right_at < len(right) and y_line > right[right_at][1]:
            right_at += 1
        
        # y_line 아래에 있는 소들 중 가장 많은 수를 below_max에 저장
        below_max = max(left_at, right_at)
        # y_line 위에 있는 소들 중 가장 많은 수를 above_max에 저장
        above_max = max(len(left) - left_at, len(right) - right_at)
        # res는 y_line 아래와 위에 있는 소들 중 가장 많은 수의 최소값을 저장
        res = min(res, max(below_max, above_max))
    
    return res


by_x = list()
n = int(input())
by_x = [tuple(map(int, input().split())) for _ in range(n)]

by_x.sort()
by_y = sorted(by_x, key = lambda x: x[1])

ans = float('inf')
x_line_at = 0
while x_line_at < len(by_x):
    x_line = by_x[x_line_at][0] + 1
    ans = min(ans, partitioning(x_line))
    # x_line보다 왼쪽에 있는 소들의 수를 증가시킴
    while x_line_at < len(by_x) and x_line > by_x[x_line_at][0]:
        x_line_at += 1

print(ans)