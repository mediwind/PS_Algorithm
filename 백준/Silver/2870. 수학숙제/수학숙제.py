import heapq as hq
import sys
input = sys.stdin.readline

n = int(input().rstrip())

Q = list()
for _ in range(n):
    string = input().rstrip()
    tmp = ''
    for s in string:
        if s.isdigit():
            tmp += s
        elif s.isalpha():
            if tmp:
                hq.heappush(Q, int(''.join(tmp)))
                tmp = ''
    
    if tmp:
        hq.heappush(Q, int(''.join(tmp)))


while Q:
    res = hq.heappop(Q)
    print(res)