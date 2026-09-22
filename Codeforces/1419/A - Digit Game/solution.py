import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if n % 2 == 1:
        has_odd = False
        for i in range(0, n, 2):
            if int(s[i]) % 2 == 1:
                has_odd = True
                break
        
        if has_odd:
            print(1)
        else:
            print(2)
            
    else:
        has_even = False
        for i in range(1, n, 2):
            if int(s[i]) % 2 == 0:
                has_even = True
                break
                
        if has_even:
            print(2)
        else:
            print(1)