import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

# 각 숫자가 배열의 어느 인덱스에 있는지 저장
pos = [0] * (n + 1)
for i in range(n):
    pos[arr[i]] = i

# x+1이 x보다 앞에 있는 경우(단절)를 카운트
breaks = 0
for i in range(1, n):
    if pos[i + 1] < pos[i]:
        breaks += 1

# 오름차순 덩어리(Run)의 개수
runs = breaks + 1

# 필요한 최소 셔플 횟수 계산
# runs보다 크거나 같은 2의 거듭제곱의 지수를 구함 (예: runs=5 -> 3)
ans = (runs - 1).bit_length()

print(ans)