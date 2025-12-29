class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict

        mp = defaultdict(list)
        for a,b,c in allowed:
            mp[(a,b)].append(c)

        seen = set()
        def dfs(cur):
            if len(cur) == 1:
                return True
            if cur in seen:
                return False
            seen.add(cur)

            nxt = []
            def build(pos, path):
                if pos == len(cur) - 1:
                    # path is next level string
                    if dfs("".join(path)):
                        return True
                    return False
                a, b = cur[pos], cur[pos+1]
                key = (a,b)
                if key not in mp:
                    return False
                for ch in mp[key]:
                    path.append(ch)
                    if build(pos+1, path):
                        return True
                    path.pop()
                return False

            return build(0, [])
            
        return dfs(bottom)