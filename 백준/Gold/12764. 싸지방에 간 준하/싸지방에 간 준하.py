import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])

# 사용 가능한 자리를 위한 최소 힙
available_seats = list()
# 현재 사용 중인 자리를 위한 최소 힙 (종료 시간, 자리 번호)
used_seats = list()

# 첫 번째 자리를 초기화
hq.heappush(available_seats, 0)
seat_usage = [0] * n

for start, end in arr:
    # 현재 시간에 사용이 끝난 자리를 다시 사용 가능하게 만듦
    while used_seats and used_seats[0][0] <= start:
        _, seat = hq.heappop(used_seats)
        hq.heappush(available_seats, seat)
    
    # 가장 작은 번호의 사용 가능한 자리를 할당
    seat = hq.heappop(available_seats)
    seat_usage[seat] += 1
    hq.heappush(used_seats, (end, seat))
    
    # 사용 가능한 자리가 없으면 새로운 자리를 추가
    if not available_seats:
        hq.heappush(available_seats, len(seat_usage))
        seat_usage.append(0)

# 사용되지 않은 자리를 필터링
seat_usage = [usage for usage in seat_usage if usage > 0]

print(len(seat_usage))
print(*seat_usage)