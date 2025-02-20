S, K = map(int, input().split())
quo = S // K  # S를 K로 나눈 몫
rem = S % K   # S를 K로 나눈 나머지

# S를 이루는 수들의 차이가 적을수록 곱의 값이 커진다.
ans = 1
for _ in range(K):
    if rem > 0:
        # 나머지가 남아있는 경우, 몫에 +1을 더한 값을 곱한다.
        # 이렇게 하면 S를 이루는 K개의 수들의 차이가 최소화된다.
        ans *= (quo + 1)
        rem -= 1
    else:
        # 나머지가 없는 경우, 몫을 그대로 곱한다.
        ans *= quo

print(ans)