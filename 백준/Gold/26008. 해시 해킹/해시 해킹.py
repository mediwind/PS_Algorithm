N, M, A = map(int, input().split())
H = int(input())

answer = pow(M, N - 1, 1000000007)
print(answer)