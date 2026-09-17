import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = [0] * 102
    for x in arr:
        count[x] += 1
        
    mex_a = 0
    while count[mex_a] > 0:
        mex_a += 1
        
    mex_b = 0
    while count[mex_b] >= 2:
        mex_b += 1
        
    print(mex_a + mex_b)