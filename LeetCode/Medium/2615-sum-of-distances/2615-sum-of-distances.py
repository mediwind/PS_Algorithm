class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        
        # 값별 인덱스 그룹화
        value_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            value_to_indices[val].append(idx)
        
        n = len(nums)
        result = [0] * n
        
        # 각 값 그룹마다 처리
        for indices in value_to_indices.values():
            k = len(indices)
            
            # prefix sum
            prefix_sum = [0] * (k + 1)
            for i in range(k):
                prefix_sum[i + 1] = prefix_sum[i] + indices[i]
            
            # 각 위치 계산
            for i in range(k):
                pos = indices[i]
                
                # 왼쪽
                left_count = i
                left_sum = prefix_sum[i]
                left_dist = pos * left_count - left_sum
                
                # 오른쪽
                right_count = k - i - 1
                right_sum = prefix_sum[k] - prefix_sum[i + 1]
                right_dist = right_sum - pos * right_count
                
                result[pos] = left_dist + right_dist
        
        return result