import sys
input = sys.stdin.readline

T, N = map(int, input().rstrip().split())
cst = [0 for _ in range(N)]

for i in range(N):
    parts = input().rstrip().split()
    cnt = int(parts[0])
    nums = list(map(int, parts[1:]))
    if len(nums) < cnt:
        nums += list(map(int, input().rstrip().split()))
    for num in nums:
        cst[i] |= (1 << (num - 1))

ans = 0
for sub in range(1 << T):
    valid = True
    for i in range(N):
        if (cst[i] & sub) == cst[i]:
            valid = False
            break
    if valid:
        ans += 1

print(ans)