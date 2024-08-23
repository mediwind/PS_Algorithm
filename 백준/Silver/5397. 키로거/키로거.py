t = int(input())
for _ in range(t):
    S = input()

    stack = list()
    tmp = list()
    for s in S:
        if s == "-":
            if stack:
                stack.pop()
        elif s == "<":
            if stack:
                tmp.append(stack.pop())
        elif s == ">":
            if tmp:
                stack.append(tmp.pop())
        else:
            stack.append(s)

    print("".join(stack) + "".join(tmp[::-1]))