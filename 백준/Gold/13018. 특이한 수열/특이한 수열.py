n, k = map(int, input().split())

if n == k:
    print("Impossible")
elif n == k + 1:
    print(' '.join(map(str, range(1, n + 1))))
else:
    result = [k + 2]
    result.extend(range(2, k + 2))
    result.extend(i + 1 if i < n else 1 for i in range(k + 2, n + 1))
    print(' '.join(map(str, result)))