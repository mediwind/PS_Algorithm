import bisect
import sys
input = sys.stdin.readline

a, b, w, M = map(int, input().rstrip().split())
flex = [int(input().rstrip()) for _ in range(a)]
fixed = []
base = [1] * w
for i in range(w):
    arr = list(map(int, input().split()))
    fixed.append(arr)
    if arr:
        base[i] = max(arr)
rem = [M - b] * w

cur_max = base[:]
avail = []
for i in range(w):
    if rem[i] > 0:
        avail.append((cur_max[i], i))
avail.sort()

flex.sort(reverse=True)

for f in flex:
    if not avail:
        print("IMPOSSIBLE")
        sys.exit(0)
    idx = bisect.bisect_left(avail, (f, -1))
    if idx < len(avail):
        cm, day = avail.pop(idx)
    else:
        cm, day = avail.pop(len(avail)-1)
    new_max = cm if cm >= f else f
    cur_max[day] = new_max
    rem[day] -= 1
    if rem[day] > 0:
        bisect.insort(avail, (cur_max[day], day))

total = 0
for i in range(w):
    if cur_max[i] > 1:
        total += 2 * (cur_max[i] - 1)
print(total)