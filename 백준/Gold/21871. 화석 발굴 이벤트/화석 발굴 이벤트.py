import sys

n, k = map(int, input().split())

# Case 1: 오염된 지역이 운동장 범위를 벗어나는 경우
if k > 2 * n:
    # 전체 칸의 수가 정답
    total_area = (2 * n + 1) * (2 * n + 1)
    print(total_area)
    sys.exit(0)

# Case 2: 오염된 지역이 운동장 내부에 있는 경우
total_area = (2 * n + 1) * (2 * n + 1)

if k % 2 == 1:
    # k가 홀수일 때의 오염된 영역 크기 계산
    # (2n-k+1)은 오염된 삼각형 영역의 한 변과 관련된 길이
    m = 2 * n - k + 1
    contaminated_area = m * (m + 2) // 2
    print(total_area - contaminated_area)
else: # k % 2 == 0
    # k가 짝수일 때의 오염된 영역 크기 계산
    # C++ 코드의 식을 그대로 사용
    # 2*n*n + 2*n*k - k*k/2 + k
    clean_area = 2 * n * n + 2 * n * k - (k * k // 2) + k
    print(clean_area)