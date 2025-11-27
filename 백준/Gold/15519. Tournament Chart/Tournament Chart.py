import sys
input = sys.stdin.readline

S = input().strip()
pos = 0

def parse():
    global pos
    if pos >= len(S):
        return None
    if S[pos] == '[':
        pos += 1
        left = parse()
        if pos < len(S) and S[pos] == '-':
            pos += 1
        right = parse()
        if pos < len(S) and S[pos] == ']':
            pos += 1
        return ('node', left, right)
    ch = S[pos]
    pos += 1
    return ('leaf', ch)

root = parse()
depths = {}
leafcnt = {}

def build(node, depth):
    t = node[0]
    if t == 'leaf':
        ch = node[1]
        depths[ch] = depth
        leafcnt[node] = 1
        return 1
    _, left, right = node
    lc = build(left, depth + 1)
    rc = build(right, depth + 1)
    total = lc + rc
    leafcnt[node] = total
    return total

total_leaves = build(root, 0)
wins = {}
lines_read = 0
while lines_read < total_leaves:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        continue
    parts = line.strip().split()
    if not parts:
        continue
    a = parts[0]
    v = int(parts[1])
    wins[a] = v
    lines_read += 1

if set(wins.keys()) != set(depths.keys()):
    print("No")
    raise SystemExit

total_matches = total_leaves - 1
if sum(wins.values()) != total_matches:
    print("No")
    raise SystemExit

for ch, depth in depths.items():
    if wins.get(ch, 0) > depth:
        print("No")
        raise SystemExit

def solve_sub(node):
    t = node[0]
    if t == 'leaf':
        ch = node[1]
        return wins[ch], wins[ch], 1
    _, L, R = node
    sumL, bestL, cntL = solve_sub(L)
    sumR, bestR, cntR = solve_sub(R)
    bestL -= 1
    bestR -= 1
    if bestL > bestR:
        best = bestL
        cnt = cntL
    elif bestL < bestR:
        best = bestR
        cnt = cntR
    else:
        best = bestL
        cnt = cntL + cntR
    total = sumL + sumR
    need = leafcnt[node] - 1
    extra = total - need
    if extra < 0 or extra != best:
        print("No")
        raise SystemExit
    if extra > 0 and cnt != 1:
        print("No")
        raise SystemExit
    return total, best, cnt

solve_sub(root)
print("Yes")