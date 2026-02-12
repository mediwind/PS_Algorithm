import sys
input = sys.stdin.readline

w, l = map(int, input().strip().split())
s = input().strip()

words = []
for _ in range(w):
    words.append(input().strip())

dp = [0] * (l + 1)

for i in range(1, l + 1):
    dp[i] = dp[i-1] + 1

    for word in words:
        word_len = len(word)

        if word_len > i:
            continue

        if word[-1] != s[i-1]:
            continue

        s_idx = i - 1
        w_idx = word_len - 1

        while s_idx >= 0 and w_idx >= 0:
            if s[s_idx] == word[w_idx]:
                w_idx -= 1
            s_idx -= 1

        if w_idx == -1:

            prev_dp_idx = s_idx + 1
            removed_count = (i - prev_dp_idx) - word_len

            dp[i] = min(dp[i], dp[prev_dp_idx] + removed_count)

print(dp[l])