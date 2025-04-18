import math
import sys
input = sys.stdin.readline


def calculate_circle_circumference(x1, y1, x2, y2, x3, y3):
    # 세 점으로 원의 중심과 반지름 계산
    # 행렬식을 이용해 원의 중심을 구함
    A = x1 * (y2 - y3) - y1 * (x2 - x3) + (x2 * y3 - x3 * y2)
    B = (x1 ** 2 + y1 ** 2) * (y3 - y2) + (x2 ** 2 + y2 ** 2) * (y1 - y3) + (x3 ** 2 + y3 ** 2) * (y2 - y1)
    C = (x1 ** 2 + y1 ** 2) * (x2 - x3) + (x2 ** 2 + y2 ** 2) * (x3 - x1) + (x3 ** 2 + y3 ** 2) * (x1 - x2)
    D = (x1 ** 2 + y1 ** 2) * (x3 * y2 - x2 * y3) + (x2 ** 2 + y2 ** 2) * (x1 * y3 - x3 * y1) + (x3 ** 2 + y3 ** 2) * (x2 * y1 - x1 * y2)

    # 원의 중심 좌표
    cx = -B / (2 * A)
    cy = -C / (2 * A)

    # 반지름 계산
    radius = math.sqrt((B ** 2 + C ** 2 - 4 * A * D) / (4 * A ** 2))

    # 원의 둘레 계산
    circumference = 2 * math.pi * radius
    return circumference


while True:
    line = input().strip()
    if not line:
        break
    try:
        x1, y1, x2, y2, x3, y3 = map(float, line.split())
        circumference = calculate_circle_circumference(x1, y1, x2, y2, x3, y3)
        print(f"{circumference:.2f}")
    except Exception:
        break