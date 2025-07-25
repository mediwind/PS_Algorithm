from itertools import combinations
import sys
# input = sys.stdin.readline


def overlap(rects):
    # rects: [(x1, y1, x2, y2), ...]
    x1 = max(r[0] for r in rects)
    y1 = min(r[1] for r in rects)
    x2 = min(r[2] for r in rects)
    y2 = max(r[3] for r in rects)
    
    if x1 < x2 and y2 < y1:
        return (x2 - x1) * (y1 - y2)
    return 0


N = int(input().rstrip())
rectangles = [list(map(int, input().rstrip().split())) for _ in range(N)]

total = 0
for k in range(1, N+1):
    for comb in combinations(rectangles, k):
        area = overlap(comb)
        
        if k % 2 == 1:
            total += area
        else:
            total -= area
            
print(total)