import sys
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())
prefix_sum = 0
prefix_max = 0
ans = []

for _ in range(n):
    h = int(input().rstrip())
    prefix_sum += h
    if h > prefix_max:
        prefix_max = h
    offset = prefix_sum - prefix_max
    
    remain = t - offset
    if remain < 0:
        completed = 0
    else:
        completed = remain // prefix_max
    
    print(str(completed + 1))