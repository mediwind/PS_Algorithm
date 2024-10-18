class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = {'a', 'e', 'i', 'o', 'u'}

        index_to_reverse = list()
        for i in range(len(s)):
            if s[i].lower() in vowel:
                index_to_reverse.append(i)
        
        mid = len(index_to_reverse) // 2
        for i in range(mid):
            st, ed = i, -(i + 1)
            s[index_to_reverse[st]], s[index_to_reverse[ed]] = s[index_to_reverse[ed]], s[index_to_reverse[st]]

        return ''.join(s)