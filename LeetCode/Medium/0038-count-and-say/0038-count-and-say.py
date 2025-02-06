class Solution:
    def countAndSay(self, n: int) -> str:
        # 초기 시퀀스를 "1"로 설정
        seq = "1"
        # n-1번 반복하여 시퀀스를 생성
        for _ in range(n - 1):
            # 현재 시퀀스를 기반으로 다음 시퀀스를 생성
            seq = self.build_sequence(seq)
        # 최종 시퀀스를 반환
        return seq

    def build_sequence(self, s: str) -> str:
        result = []  # 결과 문자열을 저장할 리스트
        count = 1    # 현재 문자의 반복 횟수

        # 문자열 s를 순회 (마지막 문자 전까지)
        for i in range(len(s) - 1):
            # 다음 문자가 현재 문자와 같으면 count 증가
            if s[i] == s[i + 1]:
                count += 1
            else:
                # 연속된 문자가 끝나면 count와 문자를 결과에 추가
                result.append(str(count))
                result.append(s[i])
                # count를 초기화
                count = 1

        # 마지막 문자를 처리
        result.append(str(count))
        result.append(s[-1])

        # 결과 리스트를 문자열로 합쳐서 반환
        return "".join(result)