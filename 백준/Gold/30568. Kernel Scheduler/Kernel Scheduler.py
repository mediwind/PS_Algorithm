import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

e1, e2 = list(), list()
for i in range(m):
    a, b = map(int, input().rstrip().split())
    
    if a > b:
        e1.append(i)
    else:
        e2.append(i)
        
if len(e1) > len(e2):
    selected = e1
else:
    selected = e2

print("YES")
print(len(selected))
print(' '.join(str(idx + 1) for idx in selected))