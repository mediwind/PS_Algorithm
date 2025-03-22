class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        # dy[j]는 nums1의 처음 i개와 nums2의 처음 j개 사이에서 교차하지 않는 최대 연결선의 개수를 저장
        dy = [0 for _ in range(m + 1)]

        # nums1의 각 원소를 순회
        for i in range(n):
            # 뒤에서부터 업데이트하여 이전 상태를 유지
            for j in range(m - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    # nums1[i]와 nums2[j]가 같으면 연결선을 추가
                    dy[j + 1] = dy[j] + 1
            
            # 현재 상태에서 dy[j + 1]과 dy[j] 중 최댓값을 유지
            for j in range(m):
                dy[j + 1] = max(dy[j + 1], dy[j])
        
        # dy[m]에는 nums1과 nums2 전체에서 교차하지 않는 최대 연결선의 개수가 저장됨
        return dy[m]