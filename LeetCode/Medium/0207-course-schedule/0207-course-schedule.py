class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = [list() for _ in range(n)]
        degree = [0 for _ in range(n)]
        for a, b in prerequisites:
            degree[a] += 1
            graph[b].append(a)
        
        Q = deque()
        visit = [0 for _ in range(n)]
        for i in range(n):
            if degree[i] == 0:
                Q.append(i)
                visit[i] = 1
        
        while Q:
            x = Q.popleft()
            for node in graph[x]:
                degree[node] -= 1
                if degree[node] == 0:
                    visit[node] = 1
                    Q.append(node)
        
        if 0 in visit:
            return False
        return True