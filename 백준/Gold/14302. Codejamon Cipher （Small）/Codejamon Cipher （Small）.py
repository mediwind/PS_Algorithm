import sys
input = sys.stdin.readline

MOD = 1000000007

T = int(input().strip())
for tc in range(1, T + 1):
    V, S = map(int, input().strip().split())

    words = []
    for _ in range(V):
        w = input().strip()
        cnt = [0] * 26
        for c in w:
            cnt[ord(c) - 97] += 1
        words.append((len(w), cnt))

    answers = []

    for _ in range(S):
        enc = input().strip()
        n = len(enc)

        pref = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            pref[i + 1] = pref[i][:]
            pref[i + 1][ord(enc[i]) - 97] += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            if dp[i] == 0:
                continue
            for L, wcnt in words:
                if i + L > n:
                    continue
                ok = True
                for c in range(26):
                    if pref[i + L][c] - pref[i][c] != wcnt[c]:
                        ok = False
                        break
                if ok:
                    dp[i + L] = (dp[i + L] + dp[i]) % MOD

        answers.append(str(dp[n]))

    print(f"Case #{tc}: " + " ".join(answers))