import sys
input = sys.stdin.readline


def date_to_num(x, y):
    x = list(map(int, x.split('-')))
    y = list(map(int, y.split('-')))
    
    start_num = (x[0] - 2000) * 12 + x[1] - 1
    end_num = (y[0] - 2000) * 12 + y[1] - 1
    
    return start_num, end_num


def num_to_date(num):
    year = str(num // 12 + 2000)
    day = str(num % 12 + 1)
    if len(day) == 1:
        day = '0' + day
    
    return year + '-' + day


prefix = [0 for _ in range((9999 - 2000 + 1) * 12 + 1)]
n = int(input())
for _ in range(n):
    start, end = input().split()
    start_num, end_num = date_to_num(start, end)
    prefix[start_num] += 1
    prefix[end_num + 1] -= 1


for i in range(1, len(prefix)):
    prefix[i] += prefix[i - 1]

maxi = 0
answer_idx = -1
for i in range(len(prefix)):
    if prefix[i] > maxi:
        maxi = prefix[i]
        answer_idx = i

print(num_to_date(answer_idx))