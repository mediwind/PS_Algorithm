t_line = input().strip()
while t_line == "":
    t_line = input().strip()
t = int(t_line)

for _ in range(t):
    s = input().strip()
    while s == "":
        s = input().strip()

    digits = [ch for ch in s if '0' <= ch <= '9']

    pos = 0
    while pos < len(digits) and digits[pos] == '0':
        pos += 1

    if pos == len(digits):
        print("0")
    else:
        print("".join(digits[pos:]))