import sys
input = sys.stdin.readline

MOD = 10**9 + 7

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    n = len(s)

    prev = None
    seq = []
    for ch in s:
        if ch == '?':
            continue
        if prev is None or ch != prev:
            seq.append(ch)
        prev = ch

    ok = True
    seen = set()
    for ch in seq:
        if ch in seen:
            ok = False
            break
        seen.add(ch)
    if not ok:
        print(0)
        continue

    ans = 1
    i = 0
    while i < n:
        if s[i] != '?':
            i += 1
            continue
        j = i
        while j < n and s[j] == '?':
            j += 1
        left = None
        right = None
        if i - 1 >= 0 and s[i - 1] != '?':
            left = s[i - 1]
        if j < n and s[j] != '?':
            right = s[j]
        seg_len = j - i
        if left is None or right is None:
            ways = 1
        else:
            ways = 1 if left == right else seg_len + 1
        ans = (ans * ways) % MOD
        i = j
        
    print(ans % MOD)