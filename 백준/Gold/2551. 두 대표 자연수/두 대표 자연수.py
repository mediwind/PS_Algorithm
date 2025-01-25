n = int(input())
arr = list(map(int, input().split()))

# 배열을 정렬
arr.sort()

# 중앙값 찾기 (아이디어 ①)
median = arr[(n - 1) // 2]

# 합계 계산
total_sum = sum(arr)

# 평균값을 반내림하여 가장 가까운 정수 찾기 (아이디어 ②)
mean_floor = total_sum // n

# 평균값과 가장 가까운 정수 찾기
# mean_floor와 mean_floor + 1 중에서 더 가까운 값을 선택
if abs(total_sum - mean_floor * n) <= abs(total_sum - (mean_floor + 1) * n):
    mean_closest = mean_floor
else:
    mean_closest = mean_floor + 1

# 결과 출력
print(median, mean_closest)