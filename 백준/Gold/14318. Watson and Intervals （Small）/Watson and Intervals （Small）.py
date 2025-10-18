import sys
input = sys.stdin.readline

t = int(input().rstrip())
for case_num in range(1, t + 1):
    n, l1, r1, a, b, c1, c2, m = map(int, input().rstrip().split())
    
    events = []
    x, y = l1, r1
    events.append((min(x, y), 0, 1))
    events.append((max(x, y) + 1, 0, -1))
    
    for i in range(1, n):
        x_new = (a * x + b * y + c1) % m
        y_new = (a * y + b * x + c2) % m
        x, y = x_new, y_new
        events.append((min(x, y), i, 1))
        events.append((max(x, y) + 1, i, -1))
    
    events.sort()
    
    active = set()
    total_coverage = 0
    unique_contribution = {}
    prev_pos = 0
    unique_start_pos = 0
    
    for pos, idx, delta in events:
        if len(active) == 0:
            prev_pos = pos
        elif len(active) == 1:
            interval_id = next(iter(active))
            unique_contribution[interval_id] = unique_contribution.get(interval_id, 0) + (pos - unique_start_pos)
        
        if delta == 1:
            active.add(idx)
        else:
            active.remove(idx)
        
        if len(active) == 0:
            total_coverage += pos - prev_pos
        elif len(active) == 1:
            unique_start_pos = pos
    
    if unique_contribution:
        max_reduction = max(unique_contribution.values())
    else:
        max_reduction = 0
    
    print(f"Case #{case_num}: {total_coverage - max_reduction}")