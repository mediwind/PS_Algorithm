import sys

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
cnt1 = A.count(1)

# 이미 쿠가 마스코트인 경우
if cnt1 >= (N + 1) // 2:
    print(0)
    sys.exit(0)

# 접두만 남기는 경우(즉 suffix를 한 번에 제거) 검사
ones = 0
for i, x in enumerate(A, start=1):
    if x == 1:
        ones += 1
    if ones >= (i + 1) // 2:
        print(1)
        sys.exit(0)

# 접미만 남기는 경우(즉 prefix를 한 번에 제거) 검사
ones = 0
for k in range(N - 1, -1, -1):
    if A[k] == 1:
        ones += 1
    length = N - k  # 남기는 접미의 길이
    if ones >= (length + 1) // 2:
        print(1)
        sys.exit(0)

# 위 경우가 아니면 2번이면 가능
print(2)