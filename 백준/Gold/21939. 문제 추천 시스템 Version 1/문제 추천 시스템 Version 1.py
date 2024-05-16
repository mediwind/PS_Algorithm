import heapq as hq
import sys
input = sys.stdin.readline

N = int(input())
maxQ = list()
minQ = list()
problems = dict()
for _ in range(N):
    p, l = map(int, input().split())
    hq.heappush(maxQ, (-l, -p))
    hq.heappush(minQ, (l, p))
    problems[p] = l
    
M = int(input())
for _ in range(M):
    order = input().split()
    order[1:] = list(map(int, order[1:]))
    if order[0] == 'add':
        hq.heappush(maxQ, (-order[2], -order[1]))
        hq.heappush(minQ, (order[2], order[1]))
        problems[order[1]] = order[2]
    elif order[0] == 'solved':
        del problems[order[1]]
    else:
        if order[1] == 1:
            while -maxQ[0][1] not in problems or problems[-maxQ[0][1]] != -maxQ[0][0]:
                hq.heappop(maxQ)
            print(-maxQ[0][1])
        else:
            while minQ[0][1] not in problems or problems[minQ[0][1]] != minQ[0][0]:
                hq.heappop(minQ)
            print(minQ[0][1])