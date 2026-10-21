import sys
input = sys.stdin.readline
 
n = int(input().strip())
parent = [0] + [int(input().strip()) for _ in range(n)]
 
max_depth = 0
 
for i in range(1, n + 1):
    depth = 0
    curr = i
    while curr != -1:
        curr = parent[curr]
        depth += 1
    if depth > max_depth:
        max_depth = depth
 
print(max_depth)