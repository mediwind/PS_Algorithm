from collections import defaultdict

# 입력 받기
h, v = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))


# y의 차이를 카운트
cnt = defaultdict(int)
for i in range(v):
    for j in range(i + 1, v):
        cnt[y[j] - y[i]] += 1

# x의 차이를 이용해 답 계산
ans = 0
for i in range(h):
    for j in range(i + 1, h):
        ans += cnt[x[j] - x[i]] # cnt에 없는 숫자여도 defaultdict(int)에 따라 자동 0으로 처리된다.

print(ans)