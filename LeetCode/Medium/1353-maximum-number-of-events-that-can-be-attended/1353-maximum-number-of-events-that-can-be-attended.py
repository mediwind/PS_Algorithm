class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # 이벤트를 시작일 기준으로 정렬
        events.sort()
        min_heap = list()
        attended_count = 0
        event_idx = 0
        total_events = len(events)
        current_day = 1

        # 이벤트가 남아있거나, 힙에 참석 가능한 이벤트가 있을 때까지 반복
        while event_idx < total_events or min_heap:
            # 오늘 시작하는 모든 이벤트를 힙에 추가 (마감일 기준)
            while event_idx < total_events and events[event_idx][0] == current_day:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1
            # 마감일이 지난 이벤트는 힙에서 제거
            while min_heap and min_heap[0] < current_day:
                heapq.heappop(min_heap)
            # 오늘 참석할 수 있는 이벤트가 있으면 하나 참석
            if min_heap:
                heapq.heappop(min_heap)
                attended_count += 1
            current_day += 1

        return attended_count