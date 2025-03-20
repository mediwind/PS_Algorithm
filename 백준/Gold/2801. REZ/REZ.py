def triangular_number(x):
    # x에 대한 삼각수를 계산
    return 1 + x * (x + 1) // 2


def find_minimum_x(target):
    # 삼각수 공식에서 triangular_number(x) >= target을 만족하는 최소 x를 탐색
    low, high = 0, 1500
    while high - low:
        mid = (low + high) // 2
        if triangular_number(mid) >= target:  # 조건을 만족하면 상한값을 줄임
            high = mid
        else:  # 조건을 만족하지 않으면 하한값을 늘림
            low = mid + 1
    return low  # 최소 x 반환


target = int(input())

# 최소 절단 횟수를 계산
num_points = find_minimum_x(target)
print(num_points)

# 절단 좌표를 생성하고 출력
max_dimension = 5000  # 케이크의 최대 좌표값
for index in range(num_points):
    # 각 절단의 시작점과 끝점을 출력
    print(max_dimension - index - 1, -5000, -5000, -max_dimension + index + 2)