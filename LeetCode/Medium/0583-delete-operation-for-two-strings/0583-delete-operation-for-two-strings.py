class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        short_len = len(word1)
        long_len = len(word2)

        previous_row = [0] * (short_len + 1)

        for i in range(long_len - 1, -1, -1):
            current_row = [0] * (short_len + 1)
            for j in range(short_len - 1, -1, -1):
                if word1[j] == word2[i]:
                    current_row[j] = 1 + previous_row[j + 1]
                else:
                    current_row[j] = max(current_row[j + 1], previous_row[j])
            previous_row = current_row

        return short_len + long_len - 2 * previous_row[0]