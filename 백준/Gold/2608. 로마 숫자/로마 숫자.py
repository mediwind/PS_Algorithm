roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

number = {
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

ans = 0
for _ in range(2):
    string = input()
    stack = list()
    for s in string:
        if stack and roman[stack[-1]] < roman[s]:
            ans += roman[s] - roman[stack[-1]]*2
        else:
            ans += roman[s]
        stack.append(s)
print(ans)

num = ans
n = len(str(num))
alpha = ''
for i in range(1, n + 1):
    place = 10 ** (n - i)
    value = num // place
#     print(i, place, value)
    if place*value in number:
        alpha += number[place*value]
    else:
        if value < 5:
            alpha += number[place] * value
        elif value > 5:
            alpha += number[5*place] + (value-5)*number[place]
    num -= value * place
print(alpha)