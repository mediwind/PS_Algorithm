class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = defaultdict(list)
        for idx, val in enumerate(arr):
            dic[val].append(idx)

        n = len(arr)
        visited = [False for _ in range(n)]
        visited[0] = True
        queue = deque([(0, 0)])

        while queue:
            x, val = queue.popleft()

            if x == n - 1:
                return val
                
            val += 1

            for r in dic[arr[x]]:
                if not visited[r]:
                    visited[r] = True
                    queue.append((r, val))
            
            dic[arr[x]].clear()

            for xx in (x - 1, x + 1):
                if 0 <= xx < n and not visited[xx]:
                    visited[xx] = True
                    queue.append((xx, val))