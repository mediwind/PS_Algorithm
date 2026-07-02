import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, l, r, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    valid_chocolates = [price for price in a if l <= price <= r]
    
    valid_chocolates.sort()
    
    count = 0
    for price in valid_chocolates:
        if k >= price:
            k -= price
            count += 1
        else:
            break
            
    print(count)