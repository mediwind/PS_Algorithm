def explode(x):
    cnt = 1
    
    now = x
    radius = 1
    left = now - 1
    while True:
        if left < 0 or hales[now] - hales[left] > radius:
            break
        while left >= 0 and hales[now] - hales[left] <= radius:
            cnt += 1
            left -= 1
        now = left + 1
        radius += 1

    now = x
    radius = 1
    right = now + 1
    while True:
        if right >= N or hales[right] - hales[now] > radius:
            break
        while right < N and hales[right] - hales[now] <= radius:
            cnt += 1
            right += 1
        now = right - 1
        radius += 1

    return cnt


N = int(input())
hales = [int(input()) for _ in range(N)]
hales.sort()

ans = float('-inf')
for i in range(N):
    ans = max(ans, explode(i))
print(ans)