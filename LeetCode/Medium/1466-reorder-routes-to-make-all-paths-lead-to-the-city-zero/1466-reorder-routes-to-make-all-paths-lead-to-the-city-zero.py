class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def DFS(city):
            nonlocal answer
            for neighbor in graph[city]:
                if neighbor in ch:
                    continue
                
                if (neighbor, city) not in roads:
                    answer += 1

                ch.add(neighbor)
                DFS(neighbor)

        roads = { (a, b) for a, b in connections }
        graph = {city: list() for city in range(n)}
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        answer = 0
        ch = {0}
        DFS(0)

        return answer