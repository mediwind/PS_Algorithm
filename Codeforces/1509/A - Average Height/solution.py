import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    odds = list()
    evens = list()
    
    for num in arr:
        if num % 2 == 1:
            odds.append(num)
        else:
            evens.append(num)
    
    ans = odds + evens
    print(*ans)