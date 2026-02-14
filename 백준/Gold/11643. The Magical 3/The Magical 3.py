import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    
    if not line or line == '0':
        break
        
    n = int(line)
    
    if n < 3:
        print("No such base")
        continue
        
    if n == 3:
        print(4)
        continue
        
    target = n - 3
    divisors = []
    
    for i in range(1, int(target**0.5) + 1):
        if target % i == 0:
            divisors.append(i)
            if i * i != target:
                divisors.append(target // i)
    
    divisors.sort()
    
    ans = -1
    for d in divisors:
        if d > 3:
            ans = d
            break
            
    if ans != -1:
        print(ans)
    else:
        print("No such base")