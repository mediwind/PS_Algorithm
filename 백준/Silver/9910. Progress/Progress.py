from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

dy = [defaultdict(int) for _ in range(n)]
max_length = 2

for i in range(n):
    for j in range(i):
        diff = nums[i] - nums[j]
        
        if dy[j][diff]:
            dy[i][diff] = dy[j][diff] + 1
        else:
            dy[i][diff] = 2
        
        max_length = max(max_length, dy[i][diff])

print(max_length)