from functools import cmp_to_key
import sys
input = sys.stdin.readline

# 비교의 기준점이 되는 혁이의 위치 (전역 변수로 사용)
pivot_point = (0, 0)

def get_point_quadrant_info(p):
    """
    점을 피벗 기준으로 어느 사분면/축에 속하는지 분류하여 정렬 우선순위를 반환합니다.
    반시계 방향 정렬을 위해 y > 0 또는 (y == 0 이고 x > 0)인 경우를 우선합니다.
    반환값: 0 (상단 반평면 또는 양의 x축), 1 (하단 반평면 또는 음의 x축)
    """
    # 피벗 기준 상대 좌표 계산
    rel_x = p[0] - pivot_point[0]
    rel_y = p[1] - pivot_point[1]

    # y좌표가 양수이거나, y가 0이고 x가 양수이면 우선순위 0
    if rel_y > 0 or (rel_y == 0 and rel_x > 0):
        return 0
    # 그 외의 경우 (y가 음수이거나, y가 0이고 x가 음수/0) 우선순위 1
    else:
        return 1

def compare_by_angle_then_distance(p1_orig, p2_orig):
    """
    두 점 p1_orig, p2_orig를 pivot_point 기준으로 다음 규칙에 따라 비교합니다:
    1. 반시계 방향 각도 순서 (작은 각도 우선)
    2. 각도가 같으면 피벗에 더 가까운 점 우선
    반환값:
        -1: p1_orig가 p2_orig보다 앞에 와야 함
         0: p1_orig와 p2_orig의 순서가 동일함
         1: p1_orig가 p2_orig보다 뒤에 와야 함
    """
    # 피벗 기준 상대 좌표 계산
    p1_rel_x, p1_rel_y = p1_orig[0] - pivot_point[0], p1_orig[1] - pivot_point[1]
    p2_rel_x, p2_rel_y = p2_orig[0] - pivot_point[0], p2_orig[1] - pivot_point[1]

    # 각 점의 정렬 우선순위 영역(반평면) 계산
    region1 = get_point_quadrant_info(p1_orig)
    region2 = get_point_quadrant_info(p2_orig)

    # 다른 영역에 속하면 영역 번호가 작은 쪽이 우선
    if region1 != region2:
        return -1 if region1 < region2 else 1

    # 같은 영역에 속하면 외적(cross product)을 이용해 각도 비교
    # 외적 = p1_rel_x * p2_rel_y - p1_rel_y * p2_rel_x
    # 외적이 양수이면 p2가 p1보다 반시계 방향으로 더 앞에 있음 (p1 우선)
    # 외적이 음수이면 p1이 p2보다 반시계 방향으로 더 앞에 있음 (p2 우선)
    cross_product = p1_rel_x * p2_rel_y - p1_rel_y * p2_rel_x

    if cross_product > 0:
        return -1 # p1이 p2보다 각도가 작음 (우선)
    elif cross_product < 0:
        return 1 # p2가 p1보다 각도가 작음 (p1이 나중)
    else:
        # 외적이 0이면 두 점은 피벗과 일직선 상에 있음
        # 거리 비교 (제곱 거리를 사용하여 sqrt 계산 방지)
        dist_sq1 = p1_rel_x**2 + p1_rel_y**2
        dist_sq2 = p2_rel_x**2 + p2_rel_y**2

        if dist_sq1 < dist_sq2:
            return -1 # p1이 더 가까움 (우선)
        elif dist_sq1 > dist_sq2:
            return 1 # p2가 더 가까움 (p1이 나중)
        else:
            return 0 # 거리도 같음 (동일 순서)



N = int(input())
points_list = [tuple(map(int, input().split())) for _ in range(N)]

pivot_point = tuple(map(int, input().split()))

points_list.sort(key=cmp_to_key(compare_by_angle_then_distance))

for point in points_list:
    print(point[0], point[1])