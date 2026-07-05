import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if sum(a) != sum(b):
        print(-1)
        continue
        
    decrease_list = []
    increase_list = []
    
    for i in range(1, n + 1):
        diff = a[i - 1] - b[i - 1]
        
        if diff > 0:
            for _ in range(diff):
                decrease_list.append(i)
        elif diff < 0:
            for _ in range(abs(diff)):
                increase_list.append(i)
                
    m = len(decrease_list)
    print(m)
    for k in range(m):
        print(decrease_list[k], increase_list[k])