N = int(input())
numbers = list(map(int, input().split()))

odd = 0
even = 0
for number in numbers:
    if number % 2:
        odd += 1
    else:
        even += 1

while odd > even:
    odd -= 2
    even += 1

if even > odd + 1:
    even = odd + 1

print(even + odd)