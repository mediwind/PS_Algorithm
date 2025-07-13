import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]
nums.sort()

ch = set()
need = 1
ans = 0
for i in range(N):
    num = nums[i]
    if num > need:
        ans += num - need
        ch.add(num - need)
        need += 1
    elif num == need:
        ch.add(num)
        need += 1

print(ans)