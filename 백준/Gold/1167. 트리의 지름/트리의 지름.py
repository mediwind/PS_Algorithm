import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

def DFS(start, result):
    for e, w in graph[start]:
        if result[e]==-1:
            result[e]=result[start]+w
            DFS(e, result)

v=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(v):
    arr=list(map(int, input().split()))
    node=arr[0]
    for i in range((len(arr)-2)//2):
        graph[node].append((arr[i*2+1], arr[i*2+2]))

res1=[-1]*(v+1)
res1[1]=0
DFS(1, res1)

maxi=max(res1)
idx=res1.index(maxi)
res2=[-1]*(v+1)
res2[idx]=0
DFS(idx, res2)
print(max(res2))