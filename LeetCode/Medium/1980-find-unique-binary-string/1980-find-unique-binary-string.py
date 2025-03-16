class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        num_set = set(nums)
        
        # 길이 n의 모든 가능한 이진 문자열을 생성
        for i in range(2 ** n):
            binary_string = bin(i)[2:]  # 이진 문자열로 변환
            # 길이 n에 맞추기 위해 앞에 '0'을 추가
            while len(binary_string) < n:
                binary_string = '0' + binary_string
            # 생성된 이진 문자열이 num_set에 포함되지 않는다면 반환
            if binary_string not in num_set:
                return binary_string