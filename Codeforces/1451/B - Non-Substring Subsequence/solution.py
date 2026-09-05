import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input().strip()
    
    for _ in range(q):
        l, r = map(int, input().split())
        
        target_left = s[l - 1]
        target_right = s[r - 1]
        
        if target_left in s[:l - 1] or target_right in s[r:]:
            print("YES")
        else:
            print("NO")