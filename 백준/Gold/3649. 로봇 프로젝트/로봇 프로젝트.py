import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())
        x *= 10000000

        n = int(input())
        legos = [int(input()) for _ in range(n)]
        legos.sort()
        legos

        lt, rt = 0, n - 1
        found = False
        while lt < rt:
            res = legos[lt] + legos[rt]
            if res == x:
                print(f'yes {legos[lt]} {legos[rt]}')
                found = True
                break
            elif res < x:
                lt += 1
            else:
                rt -= 1

        if not found:
            print('danger')
    except:
        break