class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # s = num의 변화, u = x의 변화. |s|,|u| <= t 이므로 s-u 최대는 2t
        return num + 2 * t