import sys
input = sys.stdin.readline

W, H, L, N = map(int, input().split())

# 시작점 t가 가질 수 있는 최댓값은 W + H - L
max_t = W + H - L

# imos(차이 배열) 적용을 위해 여유 있게 배열 할당
diff = [0] * (max_t + 2)

for _ in range(N):
    x, y, w, h = map(int, input().split())
    area = w * h

    # 1. t_min 계산 (우하단 꼭짓점: x+w, y 방향)
    X1, Y1 = x + w, y
    # 원점에서 (X1, Y1)로 긋는 직선이 오른쪽 변(x=W)과 먼저 만나는지 판별
    if Y1 * W <= X1 * H: 
        # 오른쪽 변과 만남: y좌표는 Y1 * W / X1
        # 가장 큰 정수를 구해야 하므로 내림(floor)
        t_min = (Y1 * W) // X1
    else:
        # 윗변과 만남: x좌표는 X1 * H / Y1
        # t = H + W - (X1 * H / Y1)
        # 파이썬의 음수 // 연산을 활용하여 안전하게 내림 처리
        t_min = H + W + (-X1 * H) // Y1

    # 2. t_max 계산 (좌상단 꼭짓점: x, y+h 방향)
    X2, Y2 = x, y + h
    if Y2 * W <= X2 * H: 
        # 오른쪽 변과 만남: y좌표는 Y2 * W / X2
        # 가장 작은 정수를 구해야 하므로 올림(ceil): (분자 + 분모 - 1) // 분모
        t_max = (Y2 * W + X2 - 1) // X2
    else:
        # 윗변과 만남: x좌표는 X2 * H / Y2
        # 올림 처리: H + W - (X2 * H // Y2)
        t_max = H + W - (X2 * H) // Y2

    # 3. 조각이 길이 L의 부채꼴에 완전히 포함되기 위한 시작점 t의 허용 구간
    l = max(0, t_max - L)
    r = min(max_t, t_min)

    # 시작점 t의 구간이 유효하다면 차이 배열에 기록
    if l <= r:
        diff[l] += area
        diff[r + 1] -= area

# 4. 차이 배열을 누적합으로 복원하며 최댓값 탐색
ans = 0
cur = 0
for t in range(max_t + 1):
    cur += diff[t]
    if cur > ans:
        ans = cur

print(ans)