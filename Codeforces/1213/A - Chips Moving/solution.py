import sys
input = sys.stdin.readline
 
n = int(input().strip())
x = list(map(int, input().split()))
 
odd_count = 0
for coord in x:
    if coord % 2 == 1:
        odd_count += 1
 
even_count = n - odd_count
 
print(min(odd_count, even_count))