import sys
input = sys.stdin.readline

W, N = map(int, input().split())
A = list(map(int, input().split()))

visited = [False] * 800001

for i in range(1, N - 1):
    for j in range(i + 1, N):
        s = A[i] + A[j]
        target = W - s

        if target > 0 and target <= 400000: # 두 수의 합 최대는 약 40만
            if visited[target]:
                print("YES")
                sys.exit(0)

    for k in range(i):
        s = A[i] + A[k]
        if s < W:
            visited[s] = True

print("NO")