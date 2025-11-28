N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

setA = set(A)
setB = set(B)

union_size = len(setA | setB)
posA = {}
posB = {}
for i, v in enumerate(A):
    posA[v] = i
for i, v in enumerate(B):
    posB[v] = i
    
freq = [0] * K
freq_rev = [0] * K
for v in setA & setB:
    p = posA[v]
    q = posB[v]
    shift = (q - p) % K
    freq[shift] += 1
    shift2 = (q + p) % K
    freq_rev[shift2] += 1
best_cycle = 0

if freq:
    best_cycle = max(best_cycle, max(freq))
if freq_rev:
    best_cycle = max(best_cycle, max(freq_rev))
    
ans = (N - union_size) + best_cycle
print(ans)