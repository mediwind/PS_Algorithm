def transform(x: int) -> int:
    return ((x << 1) if (x & 1) else (x >> 1)) ^ 6

value, steps = map(int, input().split())

seen = set()
broke_early = False

while steps > 0:
    steps -= 1
    value = transform(value)
    if value in seen:
        broke_early = True
        break
    seen.add(value)

if not broke_early:
    print(value)
else:
    sequence = [value]
    j = transform(value)
    while j != value:
        sequence.append(j)
        j = transform(j)
    cycle_len = len(sequence)
    index = (steps + cycle_len) % cycle_len
    print(sequence[index])