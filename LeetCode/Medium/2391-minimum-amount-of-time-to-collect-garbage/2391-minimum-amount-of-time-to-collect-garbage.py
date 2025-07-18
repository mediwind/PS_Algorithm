class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        last = {'M': 0, 'P': 0, 'G': 0}
        total_garbage = 0

        # 1. 각 쓰레기 종류별 마지막 집 위치와 전체 쓰레기 개수 구하기
        for i in range(n):
            for c in garbage[i]:
                last[c] = i
            total_garbage += len(garbage[i])

        # 2. 누적 이동 시간 계산
        prefix = [0 for _ in range(n)]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + travel[i - 1]

        # 3. 각 트럭의 이동 시간 합산
        total_time = total_garbage
        for c in 'MPG':
            total_time += prefix[last[c]]

        return total_time