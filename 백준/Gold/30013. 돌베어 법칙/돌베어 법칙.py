n = int(input())
record = input()

min_crickets = float('inf')

for p in range(1, n + 1):
    current_crickets = 0
    for start_offset in range(p):
        is_silent = True
        for i in range(start_offset, n, p):
            if record[i] == '#' and is_silent:
                current_crickets += 1
                is_silent = False
            elif record[i] == '.':
                is_silent = True
    
    min_crickets = min(min_crickets, current_crickets)

print(min_crickets)