N = int(input())
cards = list(map(int, input().split()))

ans = N
for i in range(N):
    for j in range(i + 1, N):
        if (cards[j] - cards[i]) % (j - i):
            continue
        
        d = (cards[j] - cards[i]) // (j - i)
        a = cards[i] - i * d
        cnt = 0
        for k in range(N):
            if cards[k] != a + k * d:
                cnt += 1
        ans = min(ans, cnt)

for i in range(N):
    cnt = sum(cards[j] != cards[i] for j in range(N))
    ans = min(ans, cnt)
print(ans)