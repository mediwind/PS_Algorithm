s = input().strip()
n = len(s)
ans = 0

for a in range(n - 1):
    seen = set()
    seen.add(s[a])
    for b in range(a + 1, n):
        if s[b] == s[a]:
            break  # s[a]가 다시 나오면 더 이상 진행 불가
        if s[b] not in seen:
            if s[b] != s[a]:
                ans += 1
        seen.add(s[b])

print(ans)