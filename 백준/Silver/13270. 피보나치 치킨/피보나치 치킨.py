N = int(input())

if N % 2:
    print(2 + (N - 3) // 2, end=' ')
else:
    print(N // 2, end=' ')

if N % 3 == 1:
    print(2 + (N - 4) // 3 * 2)
elif N % 3 == 2:
    print(1 + (N - 2) // 3 * 2)
else:
    print(N // 3 * 2)