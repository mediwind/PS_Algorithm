import sys
input = sys.stdin.readline

n = int(input().rstrip())
perm = map(int, input().rstrip().split())

stack = []
operations = []

for value in perm:
    stack.append([value, value])
    while len(stack) >= 2:
        l1, r1 = stack[-2]
        l2, r2 = stack[-1]
        new_l = min(l1, l2)
        new_r = max(r1, r2)
        if (r1 - l1 + 1) + (r2 - l2 + 1) == new_r - new_l + 1:
            stack.pop()
            stack.pop()
            stack.append([new_l, new_r])
            operations.append((new_l, new_r))
        else:
            break

if len(stack) == 1 and stack[0][0] == 1 and stack[0][1] == n:
    output = ["DA"]
    output.extend(f"{l} {r}" for l, r in operations)
    print("\n".join(output))
else:
    print("NE")