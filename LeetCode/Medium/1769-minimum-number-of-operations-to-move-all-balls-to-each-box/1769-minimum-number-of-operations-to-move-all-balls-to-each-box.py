class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        balls = [i for i in range(n) if boxes[i] == '1']
        
        ans = [0 for _ in range(n)]
        for i in range(n):
            for b in balls:
                ans[i] += abs(b - i)
        
        return ans