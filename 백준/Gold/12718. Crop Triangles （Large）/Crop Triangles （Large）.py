import sys
input = sys.stdin.readline


def comb2(n):
    return n * (n - 1) // 2 if n >= 2 else 0


def comb3(n):
    return n * (n - 1) * (n - 2) // 6 if n >= 3 else 0


t = int(input().strip())
for case in range(1, t + 1):
    parts = list(map(int, input().split()))
    n, A, B, C, D, x, y, M = parts
    counts = [0] * 9
    counts[3 * (x % 3) + (y % 3)] += 1
    for _ in range(1, n):
        x = (A * x + B) % M
        y = (C * y + D) % M
        counts[3 * (x % 3) + (y % 3)] += 1

    ans = 0
    for i in range(9):
        rx_i, ry_i = divmod(i, 3)
        for j in range(i, 9):
            rx_j, ry_j = divmod(j, 3)
            for k in range(j, 9):
                rx_k, ry_k = divmod(k, 3)
                if (rx_i + rx_j + rx_k) % 3 == 0 and (ry_i + ry_j + ry_k) % 3 == 0:
                    if i == j == k:
                        ans += comb3(counts[i])
                    elif i == j:
                        ans += comb2(counts[i]) * counts[k]
                    elif j == k:
                        ans += counts[i] * comb2(counts[j])
                    else:
                        ans += counts[i] * counts[j] * counts[k]

    print(f"Case #{case}: {ans}")