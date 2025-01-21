N, M, A = map(int, input().split())
H = int(input())

answer = 1
for i in range(N - 1):
    answer *= M
    answer %= 1000000007

print(answer)