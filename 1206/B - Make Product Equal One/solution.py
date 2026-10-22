import sys
input = sys.stdin.readline
 
n = int(input().strip())
a = list(map(int, input().split()))
 
cost = 0
neg_count = 0
zero_count = 0
 
for x in a:
    if x > 0:
        cost += x - 1
    elif x < 0:
        cost += -1 - x
        neg_count += 1
    else:
        cost += 1
        zero_count += 1
 
if neg_count % 2 == 1:
    if zero_count == 0:
        cost += 2
 
print(cost)