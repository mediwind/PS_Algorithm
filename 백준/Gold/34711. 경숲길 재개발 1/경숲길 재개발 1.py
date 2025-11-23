N = int(input())
ans = 2 * N - bin(N).count("1")
print(ans)