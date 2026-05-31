import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    software_list = sorted(zip(a, b))
    
    for req, reward in software_list:
        if k >= req:
            k += reward
        else:
            break
            
    print(k)