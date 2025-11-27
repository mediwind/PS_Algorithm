import sys

sys.setrecursionlimit(10000)

S = sys.stdin.readline().strip()
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
    leafcnt[node] = lc + rc
    return lc + rc

total_leaves = build(root, 0)
wins = {}
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, v = line.split()
    v = int(v)
    if a in wins:
        print("No")
        sys.exit(0)
    wins[a] = v

if set(wins.keys()) != set(depths.keys()):
    print("No")
    sys.exit(0)

total_matches = total_leaves - 1
if sum(wins.values()) != total_matches:
    print("No")
    sys.exit(0)

for ch, depth in depths.items():
    if wins[ch] > depth:
        print("No")
        sys.exit(0)

def solve(node, depth):
    t = node[0]
    if t == 'leaf':
        ch = node[1]
        return wins[ch], wins[ch], 1
    _, left, right = node
    sumL, bestL, cntL = solve(left, depth + 1)
    sumR, bestR, cntR = solve(right, depth + 1)
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
        sys.exit(0)
    if extra > 0 and cnt != 1:
        print("No")
        sys.exit(0)
    return total, best, cnt

solve(root, 0)
print("Yes")