import sys
N = int(input().strip())

pattern = ["*"]

for _ in range(N):
    h = len(pattern)
    w = len(pattern[0])
    
    new = [[" " for _ in range(w * 5)] for __ in range(h * 5)]
    
    positions = [
        (0, 2),
        (1, 2),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 1), (3, 2), (3, 3),
        (4, 1), (4, 3)
    ]
    
    for pr, pc in positions:
        for r in range(h):
            row = pattern[r]
            base_r = pr * h + r
            base_c = pc * w
            for c in range(w):
                if row[c] == "*":
                    new[base_r][base_c + c] = "*"
    
    pattern = ["".join(row) for row in new]

print("\n".join(pattern))