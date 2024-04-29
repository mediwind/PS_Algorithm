def romanToInt(s):
    ans = 0

    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]

    return ans


def intToRoman(num):
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


m = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

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
    1000: 'M'
}

number = 0
for _ in range(2):
    string = input()
    number += romanToInt(string)
print(number)
print(intToRoman(number))