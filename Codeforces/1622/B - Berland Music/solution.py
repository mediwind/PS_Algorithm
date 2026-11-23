import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    s = input().strip()
    
    disliked = []
    liked = []
    
    for i in range(n):
        if s[i] == '0':
            disliked.append((p[i], i))
        else:
            liked.append((p[i], i))
            
    disliked.sort()
    liked.sort()
    
    q = [0] * n
    rating = 1
    
    for _, idx in disliked:
        q[idx] = rating
        rating += 1
        
    for _, idx in liked:
        q[idx] = rating
        rating += 1
        
    print(*q)