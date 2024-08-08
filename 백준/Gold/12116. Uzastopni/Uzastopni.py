import sys
input = sys.stdin.read

N = int(input().strip())

for j in range(2, int((N * 2) ** 0.5) + 1):
    temp = N - (j * (j + 1) // 2)
    if temp % j == 0:
        print(temp // j + 1, temp // j + j)