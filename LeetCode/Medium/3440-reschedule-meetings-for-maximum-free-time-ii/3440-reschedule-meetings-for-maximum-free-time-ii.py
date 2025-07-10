class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = list()
        prev_end = 0
        for i in range(n):
            gap = startTime[i] - prev_end
            gaps.append(gap)
            prev_end = endTime[i]
        gaps.append(eventTime - endTime[-1])

        max_gap_prefix = [0 for _ in range(n)]
        max_gap_suffix = [0 for _ in range(n)]
        max_gap_prefix[0] = gaps[0]
        max_gap_suffix[-1] = gaps[-1]

        for i in range(1, n):
            max_gap_prefix[i] = max(max_gap_prefix[i - 1], gaps[i])
        for i in range(n - 1, 0, -1):
            max_gap_suffix[i - 1] = max(max_gap_suffix[i], gaps[i])

        answer = 0
        for i in range(n):
            merged_gap = gaps[i] + gaps[i + 1]
            meeting_length = endTime[i] - startTime[i]
            can_fit = False
            if i - 1 >= 0:
                can_fit = can_fit or max_gap_prefix[i - 1] >= meeting_length
            if i + 1 < n:
                can_fit = can_fit or max_gap_suffix[i + 1] >= meeting_length
            if can_fit:
                merged_gap += meeting_length
            answer = max(answer, merged_gap)

        return answer