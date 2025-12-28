class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        positions = [i for i, v in enumerate(nums) if v == x]
        m = len(positions)
        return [positions[q - 1] if 1 <= q <= m else -1 for q in queries]