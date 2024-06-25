import sys
input = sys.stdin.readline


def growing():
    m, n = map(int, input().split())
    larva = [1] * (2 * m - 1)

    for _ in range(n):
        zero, one, two = map(int, input().split())

        for j in range(zero, zero + one):
            larva[j] += 1
        for j in range(zero + one, len(larva)):
            larva[j] += 2

    return m, larva


m, larva = growing()

for i in range(m):
    print(larva[m - i - 1], end=' ')
    for j in range(1, m):
        print(larva[m + j - 1], end=' ')
    print()