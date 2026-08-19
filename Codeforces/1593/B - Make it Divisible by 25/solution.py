import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().strip()
    
    targets = ["00", "50", "25", "75"]
    ans = len(s)
    
    for target in targets:
        ptr = 1
        deletions = 0
        
        for ch in reversed(s):
            if ch == target[ptr]:
                ptr -= 1
                if ptr < 0:
                    break
            else:
                deletions += 1
                
        if ptr < 0:
            ans = min(ans, deletions)
            
    print(ans)