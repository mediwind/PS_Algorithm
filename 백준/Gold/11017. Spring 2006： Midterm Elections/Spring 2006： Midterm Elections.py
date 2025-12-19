from bisect import bisect_right
import sys
input = sys.stdin.readline

k = int(input().strip())

for data_set in range(1, k + 1):
    n = int(input().strip())
    votes = [int(input().strip()) for _ in range(n)]
    v1 = votes[0]

    possible = True
    if n == 1:
        possible = True
    else:
        others = votes[1:]
        possible = False

        # 후보 1을 마지막에 두고, 그 바로 위 후보 p를 하나씩 시도
        for p in sorted(others, reverse=True):
            t = 2 * v1 + p

            remaining = others[:]
            remaining.remove(p)
            remaining.sort()

            head = p
            ok = True

            # 뒤에서부터(=p 앞쪽으로) 하나씩 붙여서 인접합 <= t를 만족하는지 확인
            while remaining:
                limit = t - head
                idx = bisect_right(remaining, limit) - 1
                if idx < 0:
                    ok = False
                    break
                head = remaining.pop(idx)

            if ok:
                possible = True
                break

    print(f"Data Set {data_set}:")
    print("Possible" if possible else "Impossible")
    print()