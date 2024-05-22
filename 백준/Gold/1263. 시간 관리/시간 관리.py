import sys
input = sys.stdin.readline


def simulation(hour):
    start = hour
    end = start + works[0][0]
    for i in range(1, N):
        if works[i][1] - works[i][0] < end:
            return False
        else:
            start = end
            end = start + works[i][0]
    
    return True
    

N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
works.sort(key = lambda x: (x[1], x[0]))

res = float('-inf')
lt, rt = 0, works[0][1] - works[0][0]
while lt <= rt:
    mid = (lt + rt) // 2
    if simulation(mid):
        lt = mid + 1
        res = max(res, mid)
    else:
        rt = mid - 1

if res == float('-inf'):
    print(-1)
else:
    print(res)