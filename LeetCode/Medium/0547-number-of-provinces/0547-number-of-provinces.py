class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def DFS(node):
            ch.add(node)
            for i in range(n):
                if i not in ch and isConnected[node][i]:
                    DFS(i)

        
        n = len(isConnected)
        answer = 0
        ch = set()
        for node in range(n):
            if not node in ch:
                DFS(node)
                answer += 1
        
        return answer