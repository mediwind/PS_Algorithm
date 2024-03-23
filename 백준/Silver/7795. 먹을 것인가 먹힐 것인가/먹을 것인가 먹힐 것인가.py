def bs(arr, x):
    lt, rt = 0, len(arr) - 1
    res = float('-inf')
    while lt <= rt:
        m = (lt + rt) // 2
        if arr[m] < x:
            res = max(res, m)
            lt = m + 1
        else:
            rt = m - 1
    
    if res == float('-inf'):
        return 0
    return res + 1


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    answer = 0
    for i in a:
        answer += bs(b, i)
    print(answer)
