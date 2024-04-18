n, m = map(int, input().split())

board = [input() for _ in range(n)]
lines = dict()

k = int(input())
for bd in board:
    zeros = bd.count('0')
    
    if zeros > k or (zeros % 2 != k % 2):
        continue
    
    if bd not in lines:
        lines[bd] = 1
    else:
        lines[bd] += 1

ans = 0
for val in lines.values():
    ans = max(ans, val)
print(ans)