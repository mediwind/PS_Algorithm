class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        res = []
        for cd, bl, act in zip(code, businessLine, isActive):
            if not act or bl not in order or not cd:
                continue
                
            ok = all(ch.isalnum() or ch == '_' for ch in cd)

            if not ok:
                continue

            res.append((order[bl], cd))
        res.sort()

        return [cd for _, cd in res]