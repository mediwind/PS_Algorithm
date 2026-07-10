import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    bigrams = input().split()
    
    ans = bigrams[0]
    
    for i in range(1, n - 2):
        if bigrams[i - 1][1] == bigrams[i][0]:
            ans += bigrams[i][1]
        else:
            ans += bigrams[i]
            
    if len(ans) < n:
        ans += 'a'
        
    print(ans)