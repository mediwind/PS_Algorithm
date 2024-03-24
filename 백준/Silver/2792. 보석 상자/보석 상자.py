import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

lt, rt = 1, max(arr)
answer = float('inf')
while lt <= rt:
    mid = (lt + rt) // 2
#     print('lt:', lt, 'rt:', rt, 'mid:', mid)
    tmp = 0
    for a in arr:
        quo = a // mid
        rem = a % mid
        
        tmp += quo
        if rem:
            tmp += 1
    
    if tmp <= n:
        answer = min(answer, mid)
        rt = mid - 1
    else:
        lt = mid + 1
#     print('tmp:', tmp, 'answer:', answer)

print(answer)