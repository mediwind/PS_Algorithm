class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return encodedText

        cols = math.ceil(len(encodedText) / rows)
        res = list()

        for start in range(cols):
            r, c = 0, start
            while r < rows and c < cols:
                res.append(encodedText[r * cols + c])
                r += 1
                c += 1

        return ''.join(res).rstrip()