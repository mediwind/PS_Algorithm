class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1: 'I', 
            4: 'IV', 
            5: 'V', 
            9: 'IX', 
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'}
        
        answer = ''
        for key in list(roman.keys())[::-1]:
            if key > num:
                continue
            
            cnt = num // key
            # print(num, key, cnt)
            answer += roman[key] * cnt
            num %= key
            # print(num)
        
        return answer