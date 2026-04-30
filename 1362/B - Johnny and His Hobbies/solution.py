t = int(input())
for _ in range(t):
    n = int(input())
    S = set(map(int, input().split()))
    for k in range(1, 1024 + 1):
        tmp = set()
        for s in S:
            tmp.add(s ^ k)
            
        if tmp == S:
            print(k)
            break
    else:
        print(-1)