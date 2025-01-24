N, M = map(int, input().split())

# 알파벳 빈도수를 저장할 리스트 초기화
h = [0 for _ in range(26)]

# 각 줄에 대해 처리
for i in range(N):
    t = (i + 1) * (2 * N - i) + (i + N + 1) * (N - i)
    s = input().strip()
    for j in range(M):
        r = (j + 1) * (2 * M - j) + (j + M + 1) * (M - j)
        h[ord(s[j]) - ord('A')] += t * r

for count in h:
    print(count)