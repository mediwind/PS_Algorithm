class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        from collections import deque, defaultdict
        
        meetings.sort(key=lambda x: x[2])
        have = {0, firstPerson}
        i = 0
        m = len(meetings)
        while i < m:
            t = meetings[i][2]
            adj = defaultdict(list)
            nodes = set()
            
            while i < m and meetings[i][2] == t:
                x, y, _ = meetings[i]
                adj[x].append(y)
                adj[y].append(x)
                nodes.add(x); nodes.add(y)
                i += 1
            visited = set()
            to_gain = set()
            
            for start in nodes:
                if start in visited:
                    continue
                comp = []
                dq = deque([start])
                visited.add(start)
                has_secret = False
                while dq:
                    u = dq.popleft()
                    comp.append(u)
                    if u in have:
                        has_secret = True
                    for v in adj[u]:
                        if v not in visited:
                            visited.add(v)
                            dq.append(v)
                if has_secret:
                    to_gain.update(comp)
            have.update(to_gain)

        return list(have)