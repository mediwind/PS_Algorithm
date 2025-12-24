import sys
input = sys.stdin.readline

case_no = 1

while True:
    n = int(input().strip())
    if n == 0:
        break

    boxes = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        boxes.append((a, b, c))

    bases = []
    orient_count = []
    for a, b, c in boxes:
        opts = set()
        opts.add(tuple(sorted((a, b))))
        opts.add(tuple(sorted((a, c))))
        opts.add(tuple(sorted((b, c))))
        opts = list(opts)
        bases.append(opts)
        orient_count.append(len(opts))

    max_mask = 1 << n
    dp = [[[0] * orient_count[i] for i in range(n)] for _ in range(max_mask)]

    best = 0
    for i in range(n):
        for oi in range(orient_count[i]):
            dp[1 << i][i][oi] = 1
            if best < 1:
                best = 1

    for mask in range(max_mask):
        for i in range(n):
            for oi in range(orient_count[i]):
                cur = dp[mask][i][oi]
                if cur == 0:
                    continue

                bottom_a, bottom_b = bases[i][oi]

                for j in range(n):
                    if mask & (1 << j):
                        continue
                    for oj in range(orient_count[j]):
                        top_a, top_b = bases[j][oj]
                        if top_a <= bottom_a and top_b <= bottom_b:
                            nmask = mask | (1 << j)
                            cand = cur + 1
                            if cand > dp[nmask][j][oj]:
                                dp[nmask][j][oj] = cand
                                if cand > best:
                                    best = cand

    print(f"Case {case_no}: {best}")
    case_no += 1