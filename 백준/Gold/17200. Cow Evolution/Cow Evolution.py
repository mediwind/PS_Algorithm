from itertools import combinations

n = int(input())
cows = list()
all_chars = set()
for _ in range(n):
    chars = set(input().split()[1:])
    cows.append(chars)
    all_chars.update(chars)

# cows
# all_chars

for comb in combinations(all_chars, 2):
    A, B = comb
    both, only_A, only_B = False, False, False
    for cow in cows:
        has_A = A in cow
        has_B = B in cow
        
        if has_A and has_B:
            both = True
        elif has_A and not has_B:
            only_A = True
        elif not has_A and has_B:
            only_B = True
    
    if only_A and only_B and both:
        print('no')
        exit()

print('yes')