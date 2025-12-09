import sys
input = sys.stdin.readline

def first_odd_index(s):
        for i, ch in enumerate(s):
            if (ord(ch) - ord('0')) % 2 == 1:
                return i
        return -1

t = int(input().strip())
for tc in range(1, t + 1):
    s = input().strip()
    n = int(s)

    idx = first_odd_index(s)
    if idx == -1:
        print(f"Case #{tc}: 0")
        continue

    digs = [int(ch) for ch in s]

    down = digs[:]
    down[idx] -= 1
    for k in range(idx + 1, len(down)):
        down[k] = 8
    down_val = int(''.join(map(str, down)))

    up = digs[:]
    j = idx
    up[j] += 1
    while j >= 0 and up[j] == 10:
        up[j] = 0
        j -= 1
        if j >= 0:
            up[j] += 1
        else:
            up.insert(0, 1)
            j = 0
            break
    if up[j] % 2 == 1:
        up[j] += 1
        while j >= 0 and up[j] == 10:
            up[j] = 0
            j -= 1
            if j >= 0:
                up[j] += 1
            else:
                up.insert(0, 1)
                j = 0
                break
    for k in range(j + 1, len(up)):
        up[k] = 0
    up_val = int(''.join(map(str, up)))

    ans = min(n - down_val, up_val - n)
    print(f"Case #{tc}: {ans}")