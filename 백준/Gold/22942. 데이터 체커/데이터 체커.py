import heapq
import sys
input = sys.stdin.readline

N = int(input())
flag = False
Q = list()
stack = list()

for i in range(N):
    x, r = map(int, input().split())
    heapq.heappush(Q, (x-r, i))
    heapq.heappush(Q, (x+r, i))

while Q:
    if not stack:
        stack.append(heapq.heappop(Q)[1])
    else:
        number = heapq.heappop(Q)[1]
        if stack[-1] == number:
            stack.pop()
        else:
            stack.append(number)

if not stack:
    print("YES")
else:
    print("NO")