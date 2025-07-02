class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list()
        left, right = 1, k + 1

        # 먼저 k+1개의 숫자를 zigzag로 배치
        while left <= right:
            if left == right:
                res.append(left)
            else:
                res.append(left)
                res.append(right)
            left += 1
            right -= 1

        # 나머지는 순서대로 이어붙임
        for i in range(k + 2, n + 1):
            res.append(i)
            
        return res