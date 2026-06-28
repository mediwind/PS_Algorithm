import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    
    for i in range(1, n + 1):
        nested = "(" * i + ")" * i
        
        simple = "()" * (n - i)
        
        print(nested + simple)