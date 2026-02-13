from collections import deque
import sys
input = sys.stdin.readline

case_num = 1

while True:
    line = input().strip()
    if line == "0=0":
        break

    lhs_str, rhs_str = line.split('=')
    target = int(rhs_str)
    n = len(lhs_str)

    queue = deque()
    parent = {}

    for length in range(1, 6):
        if length > n:
            break

        sub = lhs_str[:length]

        if length > 1 and sub.startswith('0'):
            continue

        val = int(sub)

        if val == 0:
            continue

        if val > target:
            continue

        state = (length, val)
        if state not in parent:
            parent[state] = length
            queue.append(state)

    found = False

    while queue:
        curr_idx, curr_sum = queue.popleft()

        if curr_idx == n:
            if curr_sum == target:
                found = True
                break
            continue

        for length in range(1, 6):
            if curr_idx + length > n:
                break

            sub = lhs_str[curr_idx : curr_idx + length]

            if length > 1 and sub.startswith('0'):
                continue

            val = int(sub)
            if val == 0:
                continue

            next_sum = curr_sum + val

            if next_sum > target:
                continue

            next_state = (curr_idx + length, next_sum)

            if next_state not in parent:
                parent[next_state] = length
                queue.append(next_state)

    print(f"{case_num}. ", end="")
    if found:
        path = []
        curr_idx = n
        curr_sum = target

        while curr_idx > 0:
            length = parent[(curr_idx, curr_sum)]

            val_str = lhs_str[curr_idx - length : curr_idx]
            path.append(val_str)

            curr_sum -= int(val_str)
            curr_idx -= length

        print("+".join(path[::-1]) + "=" + rhs_str)
    else:
        print("IMPOSSIBLE")

    case_num += 1