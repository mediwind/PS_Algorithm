class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = list()  # 결과를 저장할 리스트
        n = len(s)  # 입력 문자열의 길이

        # 백트래킹을 사용하여 가능한 모든 조합을 생성하는 함수.
        def backtrack(index: int, current_permutation: list):
            # 종료 조건: 문자열의 모든 문자를 처리한 경우
            if index == n:
                result.append("".join(current_permutation))  # 리스트를 문자열로 변환하여 결과에 추가
                return

            char = s[index]  # 현재 처리 중인 문자

            # 문자가 알파벳인 경우
            if char.isalpha():
                # 1. 소문자로 추가
                current_permutation.append(char.lower())
                backtrack(index + 1, current_permutation)  # 다음 문자로 이동
                current_permutation.pop()  # 백트래킹: 마지막 문자 제거

                # 2. 대문자로 추가
                current_permutation.append(char.upper())
                backtrack(index + 1, current_permutation)  # 다음 문자로 이동
                current_permutation.pop()  # 백트래킹: 마지막 문자 제거
            # 문자가 숫자인 경우
            else:
                current_permutation.append(char)  # 숫자는 그대로 추가
                backtrack(index + 1, current_permutation)  # 다음 문자로 이동
                current_permutation.pop()  # 백트래킹: 마지막 문자 제거

        backtrack(0, [])
        return result