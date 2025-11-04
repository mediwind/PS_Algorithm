import sys
input = sys.stdin.readline


def enumerate_cuts(number: str):
    n = len(number)
    if n == 1:
        yield [int(number)]
        return

    for mask in range(1 << (n - 1)):
        parts = []
        start = 0
        for i in range(n - 1):
            if mask & (1 << i):
                parts.append(int(number[start:i + 1]))
                start = i + 1
        parts.append(int(number[start:]))
        yield parts


while True:
    target_str, num_str = input().rstrip().split()
    if target_str == "0" and num_str == "0":
        break

    target = int(target_str)
    number_value = int(num_str)

    if target == number_value:
        print(target, num_str)
        continue

    best_sum = -1
    best_parts = None
    best_count = 0

    for parts in enumerate_cuts(num_str):
        total = sum(parts)
        if total > target:
            continue
        if total > best_sum:
            best_sum = total
            best_parts = parts
            best_count = 1
        elif total == best_sum:
            best_count += 1

    if best_sum == -1:
        print("error")
    elif best_count > 1:
        print("rejected")
    else:
        print(*([best_sum] + best_parts))