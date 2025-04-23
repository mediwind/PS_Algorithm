class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # 가능한 상태의 조합을 제한하기 위해 n을 3으로 제한
        n = min(n, 3)

        # presses가 0인 경우, 상태는 항상 1가지 (모든 전구가 켜져 있음)
        if presses == 0:
            return 1

        # n = 1일 때, 가능한 상태는 2가지 (on/off)
        if n == 1:
            return 2

        # n = 2일 때
        if n == 2:
            # presses가 1이면 3가지 상태, presses가 2 이상이면 4가지 상태
            return 3 if presses == 1 else 4

        # n = 3일 때
        if n == 3:
            # presses가 1이면 4가지 상태, presses가 2이면 7가지 상태, presses가 3 이상이면 8가지 상태
            if presses == 1:
                return 4
            elif presses == 2:
                return 7
            else:
                return 8