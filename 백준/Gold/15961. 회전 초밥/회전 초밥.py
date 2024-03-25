import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ch = {v:0 for v in sorted(list(set(arr)))}

eat_sushi = 1
ch[c] = 1

for i in range(k):
    sushi = arr[i] # k는 늘 n보다 작으므로 arr[i % n]은 불필요
    
    if not ch[sushi]:
        eat_sushi += 1
    ch[sushi] += 1
arr
ch
eat_sushi
max_sushi = eat_sushi

for i in range(n):
    start = arr[i % n]
    end = arr[(i + k) % n]
    
    ch[start] -= 1
    if ch[start] == 0:
        eat_sushi -= 1
    
    if ch[end] == 0:
        eat_sushi += 1
    
    ch[end] += 1
    max_sushi = max(max_sushi, eat_sushi)
#     print('start:', start, 'end:', end)
#     print('ch:', ch)
#     print('eat_sushi:', eat_sushi, 'max_sushi:', max_sushi)
#     print()

print(max_sushi)