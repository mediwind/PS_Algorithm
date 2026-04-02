import sys
import math
input = sys.stdin.readline

pts = [tuple(map(int, input().split())) for _ in range(4)]
candidates = []

# 1. 3점-1점 분할 (Case A)
# 4개의 점 중 3개를 고르는 4가지 조합
for i in range(4):
    p1, p2, p3 = [pts[j] for j in range(4) if j != i]
    p4 = pts[i]
    
    ax, ay = p1
    bx, by = p2
    cx, cy = p3
    
    # 세 점의 외심(Circumcenter) 구하기 공식
    D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    
    # D가 0이면 세 점이 일직선상에 있으므로 외심을 구할 수 없음
    if D != 0:
        ox = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / D
        oy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / D
        
        # 중심에서 세 점까지의 거리와, 나머지 1점까지의 거리
        r123 = math.hypot(ax - ox, ay - oy)
        r4 = math.hypot(p4[0] - ox, p4[1] - oy)
        
        r_target = (r123 + r4) / 2
        candidates.append((ox, oy, r_target))

# 2. 2점-2점 분할 (Case B)
# 4개의 점을 2개, 2개로 묶는 3가지 조합
pairs = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
for (i1, i2), (i3, i4) in pairs:
    ax, ay = pts[i1]
    bx, by = pts[i2]
    cx, cy = pts[i3]
    dx, dy = pts[i4]
    
    # 첫 번째 그룹의 수직이등분선: a1*x + b1*y = c1
    a1, b1 = ax - bx, ay - by
    c1 = (ax**2 - bx**2 + ay**2 - by**2) / 2
    
    # 두 번째 그룹의 수직이등분선: a2*x + b2*y = c2
    a2, b2 = cx - dx, cy - dy
    c2 = (cx**2 - dx**2 + cy**2 - dy**2) / 2
    
    # 두 직선의 교점 구하기 (크래머 공식)
    det = a1 * b2 - a2 * b1
    if det != 0:  # 평행하지 않을 때만 교점 존재
        ox = (c1 * b2 - c2 * b1) / det
        oy = (a1 * c2 - a2 * c1) / det
        
        r12 = math.hypot(ax - ox, ay - oy)
        r34 = math.hypot(cx - ox, cy - oy)
        
        r_target = (r12 + r34) / 2
        candidates.append((ox, oy, r_target))

# 3. 후보들 중 문제의 조건을 만족하는 정답 찾기
for ox, oy, r in candidates:
    # 좌표 및 반지름의 제한 범위 체크
    if not (-100000 <= ox <= 100000 and -100000 <= oy <= 100000 and 0 <= r <= 100000):
        continue
        
    # 각 점으로부터 원주까지의 최단 거리 계산
    # |중심과 점 사이의 거리 - 원의 반지름|
    dists = [abs(math.hypot(p[0] - ox, p[1] - oy) - r) for p in pts]
    
    # 네 거리의 최댓값과 최솟값 차이가 10^-3 이하라면 정답으로 인정
    if max(dists) - min(dists) <= 1e-3:
        print(f"{ox} {oy} {r}")
        sys.exit(0)