import sys
input=sys.stdin.readline

N,I,H,R=map(int,input().split())

diff=[0]*(N+2)

seen=set()

for _ in range(R):
    a,b=map(int,input().split())
    
    if a>b:
        a,b=b,a
        
    if (a,b) in seen:
        continue
        
    seen.add((a,b))
    
    if a+1<=b-1:
        diff[a+1]-=1
        diff[b]+=1

cur=0

for i in range(1,N+1):
    cur+=diff[i]
    print(H+cur)