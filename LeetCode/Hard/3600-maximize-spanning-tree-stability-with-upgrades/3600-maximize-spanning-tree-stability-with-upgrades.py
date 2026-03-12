class DSU:
    def __init__(self, n):
        self.p=list(range(n))
        self.r=[0]*n
        
    def find(self,x):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a==b:
            return False
        if self.r[a]<self.r[b]:
            a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]:
            self.r[a]+=1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        def check(x):
            dsu=DSU(n)
            upgrades=0
            used=0
            
            free=[]
            up=[]
            
            for u,v,s,m in edges:
                if m==1:
                    if s<x:
                        return False
                    if not dsu.union(u,v):
                        return False
                    used+=1
                else:
                    if s>=x:
                        free.append((u,v))
                    elif s*2>=x:
                        up.append((u,v))
            
            for u,v in free:
                if dsu.union(u,v):
                    used+=1
            
            for u,v in up:
                if used==n-1:
                    break
                if upgrades==k:
                    break
                if dsu.union(u,v):
                    upgrades+=1
                    used+=1
            
            return used==n-1
        
        lo,hi=0,10**18
        ans=-1
        
        while lo<=hi:
            mid=(lo+hi)//2
            if check(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        
        return ans