n = int(input())
prices = list(map(int, input().split()))

cnt = [0] * 4
for v in prices:
    cnt[v] += 1

ans = 0

pairs = min(cnt[0], cnt[3])
ans += 3 * pairs
cnt[0] -= pairs
cnt[3] -= pairs

pairs = min(cnt[1], cnt[2])
ans += 3 * pairs
cnt[1] -= pairs
cnt[2] -= pairs

pairs = min(cnt[0], cnt[2])
ans += 2 * pairs
cnt[0] -= pairs
cnt[2] -= pairs

pairs = min(cnt[1], cnt[3])
ans += 2 * pairs
cnt[1] -= pairs
cnt[3] -= pairs

pairs = min(cnt[0], cnt[1])
ans += pairs
cnt[0] -= pairs
cnt[1] -= pairs

pairs = min(cnt[2], cnt[3])
ans += pairs
cnt[2] -= pairs
cnt[3] -= pairs

print(ans)