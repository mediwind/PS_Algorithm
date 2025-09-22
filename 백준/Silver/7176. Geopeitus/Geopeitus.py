import sys
from itertools import product
input = sys.stdin.readline

s = input().rstrip()
while s == '':
    s = input().rstrip()

n = int(input().rstrip())
vars_order = list()
vars_map = dict()
for _ in range(n):
    line = input().rstrip()
    while line == '':
        line = input().rstrip()
    name, rhs = line.split('=', 1)
    name = name.strip()
    vars_order.append(name)
    parts = [p.strip() for p in rhs.split(',')]
    vals = list()
    for p in parts:
        if '..' in p:
            a, b = p.split('..')
            for x in range(int(a), int(b) + 1):
                vals.append(str(x))
        else:
            vals.append(str(int(p)))
    vars_map[name] = vals

for combo in product(*(vars_map[v] for v in vars_order)):
    repl = {v: combo[i] for i, v in enumerate(vars_order)}
    out = list()
    for ch in s:
        if 'a' <= ch <= 'z' and ch in repl:
            out.append(repl[ch])
        else:
            out.append(ch)
    print(''.join(out))