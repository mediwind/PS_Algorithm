import math
import sys
input = sys.stdin.readline

n = int(input())
arr = list()
# 숫자의 빈도를 저장할 리스트
num = [0] * 1000001
# 각 학생이 머리를 친 횟수를 저장할 리스트
ans = [0] * 1000001

# 학생들이 머리에 쓴 숫자를 입력받고, 빈도 리스트를 업데이트
for _ in range(n):
    x = int(input())
    num[x] += 1
    arr.append(x)

# 각 학생에 대해 머리를 친 횟수를 계산
for i in range(n):
    cnt = 0
    # 현재 학생이 머리에 쓴 숫자의 약수를 찾기 위해 루프
    for j in range(1, int(math.sqrt(arr[i])) + 1):
        if arr[i] % j == 0:
            # 약수 j에 대해 머리를 친 횟수를 증가
            cnt += num[j]
            # arr[i]가 j의 제곱이 아닌 경우, 다른 약수에 대해서도 머리를 친 횟수를 증가
            if arr[i] != j * j:
                cnt += num[arr[i] // j]
    # 현재 학생이 자신의 숫자에 대해 머리를 친 횟수를 제외하고 출력
    print(cnt - 1)
    # 결과를 저장
    ans[arr[i]] = cnt - 1