class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 0 ≤ i < 2^n 범위에서 i^(i>>1)를 계산
        return [i ^ (i >> 1) for i in range(1 << n)]