N, K = map(int, input().split())
F = int(input())
foot = {}
for _ in range(F):
    x, y = map(int, input().split())
    foot.setdefault(x, []).append(y)

pages = 1
used = 0

for line in range(1, N + 1):
    need = 1
    notes = foot.get(line, [])
    total_notes = sum(notes)

    if used + need + total_notes > K:
        pages += 1
        used = 0

    used += need

    remaining = total_notes
    for size in notes:
        while size:
            free = K - used
            if free == 0:
                pages += 1
                used = 0
                free = K
            take = min(size, free)
            used += take
            size -= take

print(pages)