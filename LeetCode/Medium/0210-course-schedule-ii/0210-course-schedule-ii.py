class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        Q = deque()

        graph = [list() for _ in range(n)]
        degree = [0 for _ in range(n)]
        for a, b in prerequisites:
            graph[b].append(a)
            degree[a] += 1
        
        answer = list()
        for i in range(n):
            if degree[i] == 0:
                Q.append(i)
                answer.append(i)
        
        while Q:
            x = Q.popleft()
            for node in graph[x]:
                degree[node] -= 1
                if degree[node] == 0:
                    Q.append(node)
                    answer.append(node)
        
        if len(answer) < n:
            return []
        return answer