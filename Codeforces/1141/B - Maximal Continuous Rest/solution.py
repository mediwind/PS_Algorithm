import sys
input = sys.stdin.readline
 
n = int(input().strip())
a = list(map(int, input().split()))
 
extended_a = a + a
 
max_rest = 0
curr_rest = 0
 
for val in extended_a:
    if val == 1:
        curr_rest += 1
        if curr_rest > max_rest:
            max_rest = curr_rest
    else:
        curr_rest = 0
 
print(max_rest)