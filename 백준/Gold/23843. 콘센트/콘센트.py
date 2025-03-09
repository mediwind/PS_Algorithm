import heapq as hq

n, m = map(int, input().split())
devices = list(map(int, input().split()))
devices.sort(reverse = True)

now_time = 0
Q = list()
for device in devices:
    if len(Q) < m:
        hq.heappush(Q, device)
    else:
        now_time = max(now_time, hq.heappop(Q))
        hq.heappush(Q, now_time + device)

print(max(now_time, max(Q)))