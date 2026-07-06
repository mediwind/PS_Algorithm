import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    inserted = 0
    
    for i in range(n):
        current_idx = (i + 1) + inserted
        
        if arr[i] > current_idx:
            inserted += arr[i] - current_idx
            
    print(inserted)