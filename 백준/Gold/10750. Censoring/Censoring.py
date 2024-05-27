s = input()
t = input()
n = len(t)
stack = list()
for x in s:
    stack.append(x)
    if x == t[-1] and stack:
        if ''.join(stack[-n:]) == t:
            for _ in range(n):
                stack.pop()
print(''.join(stack))