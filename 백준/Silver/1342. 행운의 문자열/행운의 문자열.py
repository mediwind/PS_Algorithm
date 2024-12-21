from collections import Counter


def DFS(pre, L):
    global ans
    
    if L == n:
        ans += 1
    
    for k in counter.keys():
        if counter[k] > 0 and pre != k:
            counter[k] -= 1
            DFS(k, L + 1)
            counter[k] += 1


s = input()
n = len(s)
counter = Counter(s)
ans = 0
DFS('', 0)
print(ans)