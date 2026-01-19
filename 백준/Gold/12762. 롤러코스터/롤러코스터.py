import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

# 1. dp_left[i]: i번째 기둥에서 끝나는 '가장 긴 감소하는 부분 수열'의 길이
# 즉, 왼쪽에서 내려오는 내리막 구간의 최대 길이
dp_left = [1] * N
for i in range(N):
    for j in range(i):
        if heights[j] > heights[i]: # 앞쪽 기둥이 더 높아야 내리막 성립
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)

# 2. dp_right[i]: i번째 기둥에서 시작하는 '가장 긴 증가하는 부분 수열'의 길이
# 즉, 오른쪽으로 올라가는 오르막 구간의 최대 길이
# 뒤에서부터(N-1 -> 0) 역순으로 오면서 '감소하는 수열'을 찾으면 로직이 간단해짐
dp_right = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if heights[j] > heights[i]: # 뒤쪽 기둥이 더 높아야 오르막 성립
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)

# 3. 최댓값 찾기
# 모든 지점을 변곡점(가장 낮은 지점)으로 가정했을 때의 길이 합 - 1 (중복 제거)
max_len = 0
for i in range(N):
    # 내리막 길이 + 오르막 길이 - 1 (기준점 중복)
    current_len = dp_left[i] + dp_right[i] - 1
    if current_len > max_len:
        max_len = current_len

print(max_len)