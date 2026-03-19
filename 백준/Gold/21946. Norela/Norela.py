import sys
input = sys.stdin.readline

n, m = map(int, input().split())

spells = []

for _ in range(m):
    data = list(map(int, input().split()))
    q = data[0]
    cards = data[1:]

    mask = 0
    for card in cards:
        mask |= (1 << (card - 1))

    spells.append(mask)

target = (1 << n) - 1

best_count = float('inf')
best_sequence = []

for subset in range(1 << m):
    state = 0
    used_spells = []

    for i in range(m):
        if subset & (1 << i):
            state ^= spells[i]
            used_spells.append(i + 1)

    if state == target:
        count = len(used_spells)

        if count < best_count:
            best_count = count
            best_sequence = used_spells
        elif count == best_count:
            if used_spells < best_sequence:
                best_sequence = used_spells

print(best_count)
print(*best_sequence)