class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            # n이 1일 경우, 1부터 9까지의 숫자 중 k로 나누어떨어지는 숫자의 개수를 반환
            return 9 // k
        
        total_count = 0  # "좋은 정수"의 총 개수를 저장
        half_length = n // 2  # 팰린드롬의 왼쪽 절반 길이
        valid_palindromes = set()  # 유효한 팰린드롬의 정렬된 키를 저장하는 집합

        # 유효한 팰린드롬 후보 생성
        for x in range(1, 10**half_length):
            left_part = str(x).zfill(half_length)  # 왼쪽 절반을 0으로 채워서 생성
            if not left_part.endswith('0'):  # 왼쪽 절반이 0으로 끝나지 않는 경우만 처리
                if n % 2 == 1:  # n이 홀수인 경우
                    # 가운데 숫자를 추가하여 홀수 길이의 팰린드롬 후보 생성
                    candidates = [left_part[::-1] + str(mid) + left_part for mid in range(10)]
                else:  # n이 짝수인 경우
                    # 왼쪽 절반을 뒤집어서 붙여 짝수 길이의 팰린드롬 후보 생성
                    candidates = [left_part[::-1] + left_part]
                
                for candidate in candidates:
                    if int(candidate) % k == 0:  # 후보가 k로 나누어떨어지는 경우
                        # 후보를 정렬하여 키로 변환하고 집합에 추가
                        sorted_key = "".join(sorted(candidate))
                        valid_palindromes.add(sorted_key)

        # 멀티노미얼 계수를 계산하는 헬퍼 함수
        def multinomial_coefficient(values):
            result = 1
            k = 1
            for value in values:
                for i in range(1, value + 1):
                    result *= k
                    result //= i
                    k += 1
            return result

        # 각 팰린드롬 키의 유효한 순열 개수를 계산
        for key in valid_palindromes:
            frequency = collections.Counter(key)  # 각 숫자의 빈도를 계산
            permutations = multinomial_coefficient(frequency.values())  # 모든 순열의 개수 계산
            if frequency['0']:  # 선행 0이 포함된 순열 제거
                frequency['0'] -= 1
                permutations -= multinomial_coefficient(frequency.values())
            total_count += permutations  # 유효한 순열 개수를 총 개수에 추가

        return total_count  # "좋은 정수"의 총 개수를 반환