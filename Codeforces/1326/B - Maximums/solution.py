import sys
input = sys.stdin.readline
 
n = int(input())
b = list(map(int, input().split()))
 
a = []
current_max = 0
 
for val in b:
    original = val + current_max
    a.append(original)
    
    if original > current_max:
        current_max = original
 
print(*a)