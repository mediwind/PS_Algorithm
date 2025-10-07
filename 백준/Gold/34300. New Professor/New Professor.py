import heapq

def solve():
    try:
        C = int(input())
        shirts = []
        for _ in range(C):
            shirts.append(int(input()))
    except (IOError, ValueError):
        return

    # 최대 힙을 만들기 위해 음수로 변환하여 최소 힙에 저장
    max_heap = [-s for s in shirts]
    heapq.heapify(max_heap)

    total_weeks = 0
    
    # 매주 5가지 색상의 셔츠를 입는 것을 시뮬레이션
    while True:
        # 힙에 5개 미만의 색상이 남아있으면 더 이상 완전한 주를 채울 수 없음
        if len(max_heap) < 5:
            break

        # 이번 주에 입을 셔츠 5개를 가장 많은 색상부터 선택
        used_this_week = []
        for _ in range(5):
            # 가장 많은 셔츠가 있는 색상을 pop (음수이므로 가장 작은 값)
            shirt_count = heapq.heappop(max_heap)
            used_this_week.append(shirt_count)

        # 한 주를 성공적으로 보냈으므로 주 카운트 증가
        total_weeks += 1

        # 입은 셔츠는 개수를 1 줄여서 다시 힙에 넣음
        for count in used_this_week:
            # 셔츠를 하나 입었으므로 count에 1을 더함 (음수이므로)
            new_count = count + 1
            # 셔츠가 남아있으면(0이 아니면) 다시 힙에 추가
            if new_count != 0:
                heapq.heappush(max_heap, new_count)

    # 남은 셔츠로 며칠을 더 보낼 수 있는지 계산
    # 남은 색상의 종류가 며칠을 더 갈 수 있는지 결정
    remaining_days = len(max_heap)
    
    # 총 일수 = (완전히 보낸 주의 수 * 5) + 남은 일수
    total_days = total_weeks * 5 + remaining_days
    
    print(total_days)

solve()