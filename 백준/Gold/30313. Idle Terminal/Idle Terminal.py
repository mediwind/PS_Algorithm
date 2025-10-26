import heapq

first = list(map(int, input().split()))
n, k = first[0], first[1]
nums = []
while len(nums) < n:
    nums += list(map(int, input().split()))
dur = nums

heap = []
m = min(n, k)
for i in range(m):
    heapq.heappush(heap, (dur[i], i))

next_idx = m
prev_time = 0
answer = 0

while heap:
    finish_time, _ = heapq.heappop(heap)
    gap = finish_time - prev_time
    if gap > answer:
        answer = gap
    prev_time = finish_time
    if next_idx < n:
        heapq.heappush(heap, (finish_time + dur[next_idx], next_idx))
        next_idx += 1

print(answer)