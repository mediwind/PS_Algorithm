t = int(input())
for ith in range(1, t + 1):
    n, b = map(int, input().split())
    houses = sorted(list(map(int, input().split())))

    tally = 0
    cnt = 0
    for house in houses:
        tally += house
        if tally <= b:
            cnt += 1
        else:
            break

    print(f"Case #{ith}: {cnt}")