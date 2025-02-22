class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = list()

        while columnNumber > 0:
            columnNumber -= 1  # 0-based index로 만들기
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            columnNumber //= 26

        return ''.join(result[::-1])