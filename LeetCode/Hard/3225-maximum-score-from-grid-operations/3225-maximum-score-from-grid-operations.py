class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # prefix[j][i] = column j 의 위에서 i개 합
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        # prevPick[h]
        prev_pick = [0] * (n + 1)

        # prevSkip[h]
        prev_skip = [0] * (n + 1)

        # column 1부터 순회
        for j in range(1, n):
            curr_pick = [0] * (n + 1)
            curr_skip = [0] * (n + 1)

            for curr in range(n + 1):
                for prev in range(n + 1):

                    # 현재가 더 깊게 black
                    if curr > prev:
                        score = prefix[j - 1][curr] - prefix[j - 1][prev]

                        curr_pick[curr] = max(
                            curr_pick[curr],
                            prev_skip[prev] + score
                        )

                        curr_skip[curr] = max(
                            curr_skip[curr],
                            prev_skip[prev] + score
                        )

                    # 이전이 더 깊게 black
                    else:
                        score = prefix[j][prev] - prefix[j][curr]

                        curr_pick[curr] = max(
                            curr_pick[curr],
                            prev_pick[prev] + score
                        )

                        curr_skip[curr] = max(
                            curr_skip[curr],
                            prev_pick[prev]
                        )

            prev_pick = curr_pick
            prev_skip = curr_skip

        return max(prev_pick)