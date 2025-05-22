class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        # 1. 뒤에서부터 증가가 시작되는 지점(i) 찾기
        i = -1
        for idx in range(n - 2, -1, -1):
            if nums[idx] < nums[idx + 1]:
                i = idx
                break

        if i == -1:
            nums.reverse()
            return nums

        # 2. i보다 큰 값 중 가장 오른쪽(j) 찾기
        for j in range(n - 1, i, -1):
            if nums[j] > nums[i]:
                # 3. swap
                nums[i], nums[j] = nums[j], nums[i]
                break

        # 4. i+1부터 끝까지 reverse
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums