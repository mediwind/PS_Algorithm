import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def get_len(x):
    if x == 1:
        return m
    if x in length:
        return length[x]
    info = nodes[x]
    if info[0] == 'S1':
        L = get_len(info[1])
        res = (L + 1) // 2
    elif info[0] == 'S2':
        L = get_len(info[1])
        res = L // 2
    else:
        _, a, b = info
        res = get_len(a) + get_len(b)
    length[x] = res
    return res


def query(x, k):
    while True:
        if x == 1:
            if k > m:
                return None
            return k

        info = nodes[x]

        if info[0] == 'S1':
            parent = info[1]
            k = 2 * k - 1
            x = parent

        elif info[0] == 'S2':
            parent = info[1]
            k = 2 * k
            x = parent

        else:
            _, a, b = info
            len_a = get_len(a)
            len_b = get_len(b)

            if k <= 2 * min(len_a, len_b):
                if k % 2 == 1:
                    k = (k + 1) // 2
                    x = a
                else:
                    k = k // 2
                    x = b
            else:
                if len_a > len_b:
                    if k - 2 * len_b > len_a - len_b:
                        return None
                    k = k - len_b
                    x = a
                else:
                    if k - 2 * len_a > len_b - len_a:
                        return None
                    k = k - len_a
                    x = b


m, n, q = map(int, input().split())

nodes = {}
length = {}

for _ in range(n):
    parts = input().split()
    t = parts[0]
    x, y, z = map(int, parts[1:])
    if t == 'S':
        nodes[y] = ('S1', x)
        nodes[z] = ('S2', x)
    else:
        nodes[z] = ('M', x, y)




for _ in range(q):
    x, k = map(int, input().split())
    if get_len(x) < k:
        print("none")
    else:
        ans = query(x, k)
        print(ans if ans is not None else "none")