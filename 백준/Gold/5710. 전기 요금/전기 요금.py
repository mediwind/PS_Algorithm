import sys
input = sys.stdin.readline


def price_to_watt(x):
    if x <= 200:
        return x // 2
    elif x <= 29900:
        return (x - 200) // 3 + 100
    elif x <= 4979900:
        return (x - 29900) // 5 + 10000
    else:
        return (x - 4979900) // 7 + 1000000


def watt_to_price(x):
    if x <= 100:
        return x * 2
    elif x <= 10000:
        return 200 + (x - 100) * 3
    elif x <= 1000000:
        return 200 + 29700 + (x - 10000) * 5
    else:
        return 200 + 29700 + 4950000 + (x - 1000000) * 7


while True:
    a, b = map(int, input().rstrip().split())
    if not a and not b:
        break

    total = price_to_watt(a)
    lt, rt = 0, total // 2
    while lt <= rt:
        mid = (lt + rt) // 2

        me = watt_to_price(mid)
        neighbor = watt_to_price(total - mid)

        diff = abs(me - neighbor)

        if diff < b:
            rt = mid - 1
        elif diff > b:
            lt = mid + 1
        else:
            print(watt_to_price(mid))
            break