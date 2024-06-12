N = int(input())
s = input()

simplify = list()
for i in range(0, N, 2):
    if s[i] != s[i + 1]:
        if s[i] == 'G':
            if not simplify or simplify[-1] != 'A':
                simplify.append('A')
        else:
            if not simplify or simplify[-1] != 'B':
                simplify.append('B')

# simplify

if simplify[-1] == 'B':
    print(len(simplify) - 1)
else:
    print(len(simplify))