N = int(input())
logs = list(map(int, input().split()))
valid = True
if logs[0] > 0:
    valid = False
logs[0] = 0

for i in range(N - 2, -1, -1):
    if logs[i + 1] > 0:
        if logs[i] != -1 and logs[i] != logs[i + 1] - 1:
            valid = False
            break
        logs[i] = logs[i + 1] - 1

# logs
req = logs.count(0)
plus = logs.count(-1)
if valid:
    print(req, req + plus)
else:
    print(-1)