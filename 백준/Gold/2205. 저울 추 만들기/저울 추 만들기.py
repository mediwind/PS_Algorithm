import sys
input = sys.stdin.readline


def closest_involution(x):
    sqr = 1
    
    while 2 ** sqr < x:
        sqr += 1
        
    return 2 ** sqr


n = int(input())
pair = dict()

for i in range(n, 0, -1):
    tmp = closest_involution(i)
    
    if i in pair:
        continue
        
    if tmp == i:
        pair[i] = i
    else:
        pair[i] = tmp - i
        pair[tmp - i] = i

for key in sorted(pair.keys()):
    print(pair[key])