import heapq as hq

N = int(input())
for tc in range(1, N + 1):
    T = int(input())
    NA, NB = map(int, input().split())

    Q = list()
    for _ in range(NA):
        a, b = input().split()
        a = a.split(':')
        b = b.split(':')
        a = int(a[0]) * 60 + int(a[1])
        b = int(b[0]) * 60 + int(b[1])
        hq.heappush(Q, (a, b, 0))

    for _ in range(NB):
        a, b = input().split()
        a = a.split(':')
        b = b.split(':')
        a = int(a[0]) * 60 + int(a[1])
        b = int(b[0]) * 60 + int(b[1])
        hq.heappush(Q, (a, b, 1))

    table = {0: [], 1: []}
    ans = [0, 0]
    for _ in range(NA + NB):
        start, end, station = hq.heappop(Q)

        if table[station] and table[station][0] <= start:
            hq.heappop(table[station])
        else:
            ans[station] += 1

        hq.heappush(table[1 - station], end + T)

    print(f"Case #{tc}: {ans[0]} {ans[1]}")