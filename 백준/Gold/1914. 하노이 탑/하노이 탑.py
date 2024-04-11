def DFS(n, start, end): # start 막대의 최상단 원판을, end 막대로 옮긴다.
    if n == 1:
        print(start, end)
        return
       
    DFS(n-1, start, 6 - start - end)
    print(start, end)
    DFS(n-1, 6 - start - end, end)
    
n = int(input())
print(2**n - 1)

if n <= 20:
    DFS(n, 1, 3)