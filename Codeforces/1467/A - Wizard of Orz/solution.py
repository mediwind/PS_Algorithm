import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 1:
        print("9")
    elif n == 2:
        print("98")
    else:
        ans = ["9", "8", "9"]
        
        for i in range(n - 3):
            ans.append(str(i % 10))
            
        print("".join(ans))