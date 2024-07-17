import sys
input = sys.stdin.readline

n = int(input())

stack = list()
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        stack.append(b)
    else:
        if stack and stack[-1] >= max(stack[-1] - b, 0):
            stack[-1] = max(stack[-1] - b, 0)

for i in range(len(stack) - 1, 0, -1):
    if stack[i - 1] > stack[i]:
        stack[i - 1] = stack[i]

print(sum(stack))