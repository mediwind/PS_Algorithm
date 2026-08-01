import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().rstrip()
    
    cand1 = 'a' + s
    if cand1 != cand1[::-1]:
        print("YES")
        print(cand1)
        continue
        
    cand2 = s + 'a'
    if cand2 != cand2[::-1]:
        print("YES")
        print(cand2)
        continue
        
    print("NO")