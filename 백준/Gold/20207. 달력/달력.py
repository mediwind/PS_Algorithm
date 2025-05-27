import sys
input = sys.stdin.readline


N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

# 일정 정렬:
# 1. 시작일이 빠른 순서
# 2. 시작일이 같으면, 기간이 긴 순서 (종료일이 늦은 순서)
schedules.sort(key=lambda x: (x[0], -(x[1] - x[0])))

# 달력은 1일부터 365일까지. 각 날짜의 높이를 저장.
# calendar[i]는 i번째 날의 높이 (겹쳐진 일정의 수)
calendar = [0] * 367  # 1-indexed, 366까지 사용 (365일 + 여유)

# 모든 일정을 순회하며 달력에 표시 (높이 누적)
for start_date, end_date in schedules:
    for day in range(start_date, end_date + 1):
        calendar[day] += 1

total_coating_area = 0
current_block_start_day = 0
current_block_max_height = 0
current_block_width = 0

for day in range(1, 367): # 1일부터 365일 + 마지막 블록 처리용 366일
    if calendar[day] > 0: # 현재 날짜에 일정이 있는 경우
        if current_block_start_day == 0: # 새 블록 시작
            current_block_start_day = day

        current_block_width += 1
        current_block_max_height = max(current_block_max_height, calendar[day])
    else: # 현재 날짜에 일정이 없는 경우 (또는 366일째)
        if current_block_start_day != 0: # 진행 중인 블록이 있었다면
            # 블록 면적 계산 및 추가
            total_coating_area += current_block_max_height * current_block_width

            # 블록 정보 초기화
            current_block_start_day = 0
            current_block_max_height = 0
            current_block_width = 0

print(total_coating_area)