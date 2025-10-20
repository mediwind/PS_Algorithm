from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input().rstrip())
x_counts = defaultdict(int)
y_counts = defaultdict(int)
points = []

for _ in range(n):
    x, y = map(int, input().rstrip().split())
    points.append((x, y))
    x_counts[x] += 1
    y_counts[y] += 1

total_triangles = 0
for x, y in points:
    vertical_choices = x_counts[x] - 1
    horizontal_choices = y_counts[y] - 1
    
    total_triangles += vertical_choices * horizontal_choices

print(total_triangles)