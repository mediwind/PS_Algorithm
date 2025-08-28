class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # 결과 배열 초기화
        arr = [0] * len(pref)
        # 첫 번째 원소는 pref[0] 그대로 사용
        arr[0] = pref[0]
        
        # 나머지 원소 계산
        for i in range(1, len(pref)):
            arr[i] = pref[i] ^ pref[i-1]  # XOR 연산으로 arr[i] 복원
        
        return arr