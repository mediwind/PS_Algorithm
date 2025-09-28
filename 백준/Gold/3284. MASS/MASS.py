mass = {'H':1,'C':12,'O':16}

s = input()
stack = []
for ch in s:
    if ch in mass:
        stack.append(mass[ch])
    elif ch == '(':
        stack.append('(')
    elif ch == ')':
        sm = 0
        while stack and stack[-1] != '(':
            sm += stack.pop()
        stack.pop()
        stack.append(sm)
    else:  # digit
        d = int(ch)
        v = stack.pop()
        stack.append(v * d)

print(sum(stack))