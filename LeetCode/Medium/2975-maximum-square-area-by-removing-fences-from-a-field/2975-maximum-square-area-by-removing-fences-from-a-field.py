class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        modulo = 10**9 + 7

        horizontal_diffs = set()
        vertical_diffs = set()

        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)

        hFences.sort()
        vFences.sort()

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                horizontal_diffs.add(hFences[j] - hFences[i])

        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                vertical_diffs.add(vFences[j] - vFences[i])

        max_area = 0
        for length in horizontal_diffs:
            if length in vertical_diffs:
                area = length * length
                if area > max_area:
                    max_area = area

        if max_area == 0:
            return -1

        return max_area % modulo