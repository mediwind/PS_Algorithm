import sys
input = sys.stdin.readline


def dfs(idx):
    if idx == len_a:
        for k in range(len_a, n):
            s = 0
            for i in range(len_a):
                j = k - i
                if 0 <= j < len_a:
                    s += a[i] * a[j]
            if s % 10 != c[k]:
                return  

        valid_answers.append(int("".join(map(str, a[::-1]))))
        return

    for digit in range(10):
        if idx == len_a - 1 and digit == 0:
            continue

        a[idx] = digit

        s = 0
        for i in range(idx + 1):
            j = idx - i
            if j < len_a:
                s += a[i] * a[j]
        
        if s % 10 == c[idx]:
            dfs(idx + 1)


N = input().strip()
c = list(map(int, N[::-1]))
n = len(c)

if n % 2 == 0:
    print(-1)
    sys.exit(0)

len_a = (n + 1) // 2
a = [0] * len_a

valid_answers = []



dfs(0)

if valid_answers:
    print(min(valid_answers))
else:
    print(-1)