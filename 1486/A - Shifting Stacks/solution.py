import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    current_sum = 0
    possible = True
    
    for i in range(n):
        current_sum += arr[i]
        required_sum = i * (i + 1) // 2
        
        if current_sum < required_sum:
            possible = False
            break
            
    if possible:
        print("YES")
    else:
        print("NO")