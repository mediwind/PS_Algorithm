s = input()
stack = list()

for i in s:
    stack.append(i)
    if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            stack.pop()

if stack == ['P']:
    print("PPAP")
else:
    print("NP")