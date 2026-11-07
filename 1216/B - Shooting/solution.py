import sys
input = sys.stdin.readline
 
n = int(input().strip())
a = list(map(int, input().split()))
 
cans = []
for i in range(n):
    cans.append((a[i], i + 1))
 
cans.sort(key=lambda x: x[0], reverse=True)
 
total_shots = 0
order = []
 
for k in range(n):
    durability, idx = cans[k]
    total_shots += durability * k + 1
    order.append(str(idx))
 
print(total_shots)
print(" ".join(order))