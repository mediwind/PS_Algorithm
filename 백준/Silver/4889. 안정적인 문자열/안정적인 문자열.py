tc = 1
while True:
    string = input()
    if string[0] == '-':
        break
    stack = list()
    for s in string:
        if stack and stack[-1] == '{' and s == '}':
            stack.pop()
            continue
        stack.append(s)

    ans = 0
    while stack:
        if stack[-1] != stack[-2]:
            ans += 2
        else:
            ans += 1

        for _ in range(2):
            stack.pop()

    print(f"{tc}. {ans}")
    tc += 1