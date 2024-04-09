class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        ch = [0 for _ in range(n)]
        answer = 0
        for i in range(n - 1, -1, -1):
            if ch[i]:
                continue
            
            if i == 0:
                if not ch[i]:
                    answer += roman[s[i]]
                break

            ch[i] = 1
            if roman[s[i]] > roman[s[i - 1]]:
                answer += roman[s[i]] - roman[s[i - 1]]
                ch[i - 1] = 1
            else:
                answer += roman[s[i]]
        
        return answer