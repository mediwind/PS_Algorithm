t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    
    start = 0
    cnt = 0
    for i in range(n):
        while True:
            if start == m or a[i] <= b[start]:
                cnt += start
                break
            
            start += 1

    print(cnt)