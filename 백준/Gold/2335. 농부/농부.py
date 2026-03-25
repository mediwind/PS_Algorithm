import sys
from collections import Counter
from bisect import bisect_left
input = sys.stdin.readline

Q, M, K = map(int, input().split())

gardens = list(map(int, input().split()))
fields = list(map(int, input().split()))

garden_counts = Counter(gardens)

fields.sort(reverse=True)
pref_F = [0] * (K + 1)
for i in range(K):
    pref_F[i+1] = pref_F[i] + fields[i]

min_penalty = float('inf')
mask = (1 << (Q + 1)) - 1

keys = [0] + list(garden_counts.keys())

for X in keys:
    mod_counts = dict(garden_counts)
    if X > 0:
        mod_counts[X] -= 1
        
    items = []
    for size, count in mod_counts.items():
        if count == 0: continue
        k = 1
        while count >= k:
            items.append(size * k)
            count -= k
            k *= 2
        if count > 0:
            items.append(size * count)
            
    dp = 1
    for item in items:
        dp = (dp | (dp << item)) & mask
        
    s_str = bin(dp)[2:]
    len_s = len(s_str)
    idx = -1
    
    while True:
        idx = s_str.find('1', idx + 1)
        if idx == -1:
            break
            
        S = len_s - 1 - idx
        R = Q - S
        
        if X == 0:
            if R <= 0:
                penalty = 0
            elif R > pref_F[-1]:
                penalty = float('inf')
            else:
                penalty = bisect_left(pref_F, R)
        else:
            R_prime = max(0, R - (X - 1))
            if R_prime <= 0:
                penalty = 1
            elif R_prime > pref_F[-1]:
                penalty = float('inf')
            else:
                penalty = 1 + bisect_left(pref_F, R_prime)
                
        if penalty < min_penalty:
            min_penalty = penalty

print(Q - min_penalty)