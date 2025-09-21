n = int(input())
cnt = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        cnt[j] += 1

best = 1
for i in range(2, n + 1):
    if cnt[i] > cnt[best]:
        best = i

print(best)
print(cnt[best])