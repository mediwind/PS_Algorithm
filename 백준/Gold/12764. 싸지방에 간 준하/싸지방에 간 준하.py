import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])

# 현재 사용 중인 자리 (종료 시간, 자리 번호)
used_seats = list()
# 사용 가능한 자리 번호
available_seats = list()
# 각 자리별 사용 횟수
seat_usage = list()

# 첫 번째 사람 처리
hq.heappush(used_seats, (arr[0][1], 0))
seat_usage.append(1)

for i in range(1, n):
    start, end = arr[i]
    
    # 사용이 끝난 자리를 available_seats로 이동
    while used_seats and used_seats[0][0] <= start:
        _, seat_number = hq.heappop(used_seats)
        hq.heappush(available_seats, seat_number)
    
    if available_seats:
        # 기존 자리를 사용할 때
        seat_number = hq.heappop(available_seats)
        hq.heappush(used_seats, (end, seat_number))
        seat_usage[seat_number] += 1
    else:
        # 새로운 자리가 필요할 때
        seat_number = len(seat_usage)
        hq.heappush(used_seats, (end, seat_number))
        seat_usage.append(1)

print(len(seat_usage))
print(*seat_usage)