import heapq
from collections import deque

# 입력 받기
n = int(input())
sizes = list(map(int, input().split()))

# 인형 크기별 개수 세기
count = [0] * 100100
for size in sizes:
    count[size] += 1

# 우선순위 큐 초기화
max_heap = []
for size in range(100100):
    if count[size] > 0:
        heapq.heappush(max_heap, (-size, count[size]))  # 최대 힙을 위해 음수로 저장

total_profit = 0
while max_heap:
    temp_queue = deque()
    length = 1
    max_size, count = heapq.heappop(max_heap)
    max_size = -max_size  # 음수로 저장된 값을 다시 양수로 변환
    current_size = max_size
    if count > 1:
        temp_queue.append((max_size, count - 1))

    while max_heap and -max_heap[0][0] == current_size - 1:
        length += 1
        current_size, count = heapq.heappop(max_heap)
        current_size = -current_size  # 음수로 저장된 값을 다시 양수로 변환
        if count > 1:
            temp_queue.append((current_size, count - 1))

    total_profit += max_size * length

    while temp_queue:
        heapq.heappush(max_heap, (-temp_queue[0][0], temp_queue[0][1]))
        temp_queue.popleft()

# 결과 출력
print(total_profit)