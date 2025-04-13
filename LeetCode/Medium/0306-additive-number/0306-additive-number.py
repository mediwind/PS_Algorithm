class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # 주어진 두 숫자와 남은 문자열이 additive sequence를 형성하는지 확인하는 헬퍼 함수
        def is_valid_sequence(first: int, second: int, remaining: str) -> bool:
            while remaining:
                # 다음 숫자를 계산
                next_num = str(first + second)
                # 남은 문자열이 다음 숫자로 시작하지 않으면 False 반환
                if not remaining.startswith(next_num):
                    return False
                # 첫 번째와 두 번째 숫자를 업데이트하고, 남은 문자열을 줄임
                first, second = second, int(next_num)
                remaining = remaining[len(next_num):]
            return True  # 모든 조건을 만족하면 True 반환

        n = len(num)
        # 첫 번째와 두 번째 숫자의 가능한 조합을 탐색
        for i in range(1, n):
            for j in range(i + 1, n):
                first, second = num[:i], num[i:j]
                # 숫자가 leading zero(앞에 0이 있는 경우)라면 건너뜀
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue
                # 첫 번째와 두 번째 숫자를 정수로 변환하고, additive sequence인지 확인
                if is_valid_sequence(int(first), int(second), num[j:]):
                    return True  # 조건을 만족하면 True 반환
        return False  # 모든 경우를 확인해도 조건을 만족하지 않으면 False 반환