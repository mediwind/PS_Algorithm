from collections import defaultdict

counts = list(map(int, input().split()))
dice = [(counts[0], 4), (counts[1], 6), (counts[2], 8), (counts[3], 12), (counts[4], 20)]

dist = {0: 1}
for cnt, sides in dice:
    for _ in range(cnt):
        nxt = defaultdict(int)
        for s, ways in dist.items():
            for face in range(1, sides + 1):
                nxt[s + face] += ways
        dist = nxt

result = sorted(dist.items(), key=lambda x: (-x[1], x[0]))
print(" ".join(str(total) for total, _ in result))