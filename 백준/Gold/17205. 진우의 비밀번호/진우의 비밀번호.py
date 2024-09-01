n = int(input())
pw = input()

cnt = [0 for _ in range(n + 1)]
cnt[0] = 1
for i in range(1, n + 1):
    cnt[i] = cnt[i - 1] * 26 + 1

ans = 0
for i in range(len(pw)):
    ans += (ord(pw[i]) - ord('a')) * cnt[n - i - 1] + 1

print(ans)