import sys
import heapq
input = sys.stdin.readline

Z = int(input())
for _ in range(Z):
    N = int(input().strip())
    given_sums = list(map(int, input().strip().split()))
    given_sums.sort()

    ans = []
    current_sums = [0]
    pq = []

    possible = True

    for x in given_sums:
        if pq:
            expected = pq[0]

            if expected == x:
                heapq.heappop(pq)
                continue
            elif expected < x:
                possible = False
                break

        new_val = x
        ans.append(new_val)

        new_generated_sums = []
        for s in current_sums:
            if s > 0:
                heapq.heappush(pq, s + new_val)
            new_generated_sums.append(s + new_val)

        current_sums.extend(new_generated_sums)

        if len(ans) > N:
            possible = False
            break

    if possible and len(ans) == N and not pq:
        print(*(ans))
    else:
        print("NO")