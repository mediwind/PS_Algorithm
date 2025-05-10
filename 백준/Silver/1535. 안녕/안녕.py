n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dy = [0 for _ in range(101)]

for i in range(n):
    for health in range(100, L[i] - 1, -1):
        dy[health] = max(dy[health], dy[health - L[i]] + J[i])

print(max(dy[:100]))