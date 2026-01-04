import sys
input = sys.stdin.readline

n = int(input().strip())
a = [int(input().strip()) for _ in range(n)]

L = [-1] * (n + 1)
R = [-1] * (n + 1)

for i, c in enumerate(a):
    if c == 0:
        continue
    if L[c] == -1:
        L[c] = i
    R[c] = i

stack = []
ans = 0

for i, c in enumerate(a):
    if c == 0:
        if stack:
            print(-1)
            sys.exit(0)
        continue

    if L[c] == i:
        stack.append(c)
        if len(stack) > ans:
            ans = len(stack)
    else:
        if not stack or stack[-1] != c:
            print(-1)
            sys.exit(0)

    if R[c] == i:
        if not stack or stack[-1] != c:
            print(-1)
            sys.exit(0)
        stack.pop()

if stack:
    print(-1)
else:
    print(ans)