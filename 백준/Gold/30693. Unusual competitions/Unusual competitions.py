n = int(input().strip())
s = input().strip()

balance = 0
bad_start = -1
answer = 0

for i, ch in enumerate(s):
    if ch == '(':
        balance += 1
    else:
        balance -= 1

    if balance < 0 and bad_start == -1:
        bad_start = i
    if balance == 0 and bad_start != -1:
        answer += i - bad_start + 1
        bad_start = -1

print(answer if balance == 0 else -1)