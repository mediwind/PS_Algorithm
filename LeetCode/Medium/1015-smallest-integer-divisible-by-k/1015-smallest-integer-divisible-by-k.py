class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # k가 짝수거나 5로 끝나는 경우, n은 존재하지 않음
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0  # 나머지를 저장
        for length in range(1, k + 1):  # 최대 k번 반복 (나머지는 k보다 작으므로)
            remainder = (remainder * 10 + 1) % k  # n을 1로만 구성
            if remainder == 0:  # 나머지가 0이면 k로 나누어 떨어짐
                return length

        return -1  # 루프를 다 돌았는데도 나머지가 0이 되지 않으면 -1 반환