import sys
import math
import heapq
input = sys.stdin.readline


def ratio_from_cos(cosv):
    s = math.sqrt((1.0 - cosv) * 0.5)
    return (1.0 - s) / (1.0 + s)


T = int(input())

for _ in range(T):
    a, b, k = map(int, input().split())
    a = float(a)
    b = float(b)

    c = math.hypot(a, b)

    r1 = (a + b - c) / 2.0

    q0 = (1.0 - math.sqrt(0.5)) / (1.0 + math.sqrt(0.5))
    qA = ratio_from_cos(a / c)
    qB = ratio_from_cos(b / c)

    heap = []
    heapq.heappush(heap, -r1)

    heapq.heappush(heap, -(r1 * q0))
    heapq.heappush(heap, -(r1 * qA))
    heapq.heappush(heap, -(r1 * qB))

    heap = [(-r1, None), (-(r1*q0), q0), (-(r1*qA), qA), (-(r1*qB), qB)]
    heapq.heapify(heap)

    radius = r1
    for _ in range(k):
        radius, ratio = heapq.heappop(heap)
        radius = -radius
        if ratio is not None:
            heapq.heappush(heap, (-(radius * ratio), ratio))

    area = math.pi * radius * radius
    print(f"{area:.10f}")