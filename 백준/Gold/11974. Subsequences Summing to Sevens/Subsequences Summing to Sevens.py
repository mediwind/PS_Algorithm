# 입력 처리
n = int(input())
cow_ids = [int(input()) for _ in range(n)]

# first_occurrence: 각 나머지가 처음 등장한 위치 저장
first_occurrence = [float('inf')] * 7
# last_occurrence: 각 나머지가 마지막으로 등장한 위치 저장
last_occurrence = [0] * 7
first_occurrence[0] = 0  # 누적합이 0인 경우를 처리하기 위해 초기화

current_prefix_sum = 0  # 현재 누적합
for i in range(1, n + 1):
    current_prefix_sum += cow_ids[i - 1]
    current_prefix_sum %= 7
    first_occurrence[current_prefix_sum] = min(first_occurrence[current_prefix_sum], i)
    last_occurrence[current_prefix_sum] = i

max_group_size = 0  # 결과값
for remainder in range(7):
    if first_occurrence[remainder] <= n:
        max_group_size = max(max_group_size, last_occurrence[remainder] - first_occurrence[remainder])

# 결과 계산 및 출력
print(max_group_size)