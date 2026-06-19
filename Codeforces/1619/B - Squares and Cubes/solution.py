import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    liked_numbers = set()
    
    i = 1
    while i * i <= n:
        liked_numbers.add(i * i)
        i += 1
        
    i = 1
    while i * i * i <= n:
        liked_numbers.add(i * i * i)
        i += 1
        
    print(len(liked_numbers))