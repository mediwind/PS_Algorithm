import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())

blue_time = 0
red_time = 0

res = list()

for _ in range(N):
    time, color, number = input().split()
    time, number = int(time), int(number)
    
    if color == 'B':
        blue_time = max(blue_time, time)
    else:
        red_time = max(red_time, time)
    
    for _ in range(number):
        if color == 'B':
            res.append((blue_time, 'B'))
            blue_time += A
        else:
            res.append((red_time, 'R'))
            red_time += B

res.sort(key = lambda x: (x[0], x[1]))

res_a, res_b = list(), list()
for i in range(1, len(res) + 1):
    if res[i - 1][1] == 'B':
        res_a.append(i)
    else:
        res_b.append(i)

print(len(res_a))
print(*res_a)
print(len(res_b))
print(*res_b)