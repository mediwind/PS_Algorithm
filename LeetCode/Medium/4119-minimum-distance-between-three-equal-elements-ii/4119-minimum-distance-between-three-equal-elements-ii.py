class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        pos = defaultdict(list)
        
        # 1. 위치 저장
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        INF = float('inf')
        ans = INF
        
        # 2. 각 값마다 처리
        for arr in pos.values():
            if len(arr) < 3:
                continue
            
            # 3. 연속된 3개만 확인
            for i in range(len(arr) - 2):
                dist = 2 * (arr[i+2] - arr[i])
                ans = min(ans, dist)
        
        return ans if ans != INF else -1