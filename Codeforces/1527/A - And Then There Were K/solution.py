import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    power_of_2 = 1
    while power_of_2 * 2 <= n:
        power_of_2 = power_of_2 * 2
        
    ans = power_of_2 - 1
    
    print(ans)