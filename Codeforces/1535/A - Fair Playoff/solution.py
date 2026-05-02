import sys
input = sys.stdin.readline
 
t = int(input().strip())
for _ in range(t):
    s1, s2, s3, s4 = map(int, input().strip().split())
    
    top2 = sorted([s1, s2, s3, s4], reverse = True)[:2]
    w1, w2 = max(s1, s2), max(s3, s4)
    
    if (w1 in top2) and (w2 in top2):
        print("YES")
    else:
        print("NO")