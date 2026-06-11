import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    l, r, k = map(int, input().split())
    
    if l == r:
        if l == 1:
            print("NO")
        else:
            print("YES")
    else:
        total_elements = r - l + 1
        
        if total_elements % 2 == 0:
            odds = total_elements // 2
        else:
            if l % 2:
                odds = total_elements // 2 + 1
            else:
                odds = total_elements // 2
        
        if k >= odds:
            print("YES")
        else:
            print("NO")