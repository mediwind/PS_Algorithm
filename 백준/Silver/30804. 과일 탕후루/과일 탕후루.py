n = int(input())
arr = list(map(int, input().split()))

lt = 0
ans = 0
distinct_count = 0  # 현재 슬라이딩 윈도우 내의 서로 다른 숫자의 개수
F = {}  # 각 숫자의 빈도를 저장하는 딕셔너리

for rt in range(n):
    F[arr[rt]] = F.get(arr[rt], 0) + 1  # 현재 숫자의 빈도를 증가시킴

    if F[arr[rt]] == 1:
        distinct_count += 1  # 새로운 숫자가 추가되면 distinct_count 증가

    # 서로 다른 숫자의 개수가 2개를 초과하면 윈도우를 축소
    while distinct_count > 2:
        F[arr[lt]] -= 1  # 왼쪽 끝 숫자의 빈도를 감소시킴

        if F[arr[lt]] == 0:
            distinct_count -= 1  # 숫자의 빈도가 0이 되면 distinct_count 감소

        lt += 1  # 윈도우의 왼쪽 끝을 오른쪽으로 이동

    # 현재 윈도우의 길이를 계산하고 최대 길이를 갱신
    ans = max(ans, rt - lt + 1)

print(ans)