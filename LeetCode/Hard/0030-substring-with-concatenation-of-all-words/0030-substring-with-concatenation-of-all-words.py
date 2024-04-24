from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1

        len_s = len(s)
        n = len(words)
        word_size = len(words[0])
        window_size = word_size * n

        ans = []
        for start_pos in range(word_size):  # Try all starting positions
            start = start_pos
            while start + window_size - 1 < len_s:  # Bound check
                curr = freq.copy()  # Make a copy of freq map to edit
                matched = True  # presume that match happened
                for i in range(n):  # Find each word
                    curr_word = s[start + i * word_size : start + i * word_size + word_size]  # Extract current word
                    if curr_word not in curr or curr[curr_word] == 0:  # Match word
                        matched = False  # current word did not match
                        break
                    curr[curr_word] -= 1  # Remove word after having found
                if matched:  # Found match
                    ans.append(start)
                start += word_size  # Sliding Window
        return ans