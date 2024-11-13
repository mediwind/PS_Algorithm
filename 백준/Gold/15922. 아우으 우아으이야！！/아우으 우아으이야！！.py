n = int(input())
intervals = [list(map(int, input().split())) for _ in range(n)]

intervals.sort()

total_length = 0
start, end = intervals[0]

for i in range(1, n):
    current_start, current_end = intervals[i]
    if end > current_start:
        end = max(end, current_end)
    else:
        total_length += end - start
        start, end = current_start, current_end

total_length += end - start

print(total_length)