N, K = map(int, input().split())
ans = list()
nums = list(range(1, N + 1))

for i in range(N):
    # 남은 자리수
    remain = N - i - 1
    # 이 자리에 놓을 수 있는 최대 inversion 수
    if K >= remain:
        # 맨 뒤에 있는 가장 큰 수를 앞으로 뽑아 inversion을 최대한 만듦
        ans.append(nums.pop())
        K -= remain
    else:
        # inversion을 더 만들 수 없으니, 남은 수 중 K번째 뒤에 있는 수를 앞으로
        ans.append(nums.pop(K))
        ans += nums
        break

print(*ans)