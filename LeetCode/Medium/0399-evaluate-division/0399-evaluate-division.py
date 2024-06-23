class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def BFS(start, end):
            Q, visit = deque(), set()
            Q.append((start, 1))
            visit.add(start)

            while Q:
                node, weight = Q.popleft()
                if node == end:
                    return weight
                
                for next_node, next_weight in graph[node]:
                    if next_node not in visit:
                        Q.append((next_node, weight * next_weight))
                        visit.add(next_node)

            return -1

            
        n = len(equations)
        graph = defaultdict(list)
        for i in range(n):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
        
        answer = list()
        for a, b in queries:
            if a not in graph or b not in graph:
                answer.append(-1)
                continue
            
            answer.append(BFS(a, b))
        
        return answer