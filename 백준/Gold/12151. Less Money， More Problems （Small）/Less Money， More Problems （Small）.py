import sys
input = sys.stdin.readline

T = int(input().rstrip())
for case in range(1, T + 1):
    C, D, V = map(int, input().rstrip().split())
    denoms = list(map(int, input().rstrip().split()))
    
    idx = 0
    reach = 0
    added = 0
    while reach < V:
        if idx < D and denoms[idx] <= reach + 1:
            reach += denoms[idx] * C
            idx += 1
        else:
            reach += (reach + 1) * C
            added += 1
            
    print(f"Case #{case}: {added}")