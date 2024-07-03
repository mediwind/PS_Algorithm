class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def DFS(L, start):
            if L == k:
                answer.append(res[:]) # 리스트를 각 재귀에서 독립적 상태로 기록하고 싶다면 반드시 복사[:]한 뒤 진행
                return
            
            for i in range(start, n + 1):
                res[L] = i
                DFS(L + 1, i + 1)
        
        answer = list()
        res = [0 for _ in range(k)]
        DFS(0, 1)
        return answer