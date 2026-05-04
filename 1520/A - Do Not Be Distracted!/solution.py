import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    orders = input()
    previous = {orders[0]}
    
    for i in range(1, n):
        now = orders[i]
        if (orders[i - 1] != now) and (now in previous):
            print("NO")
            break
            
        previous.add(now)
    else:
        print("YES")