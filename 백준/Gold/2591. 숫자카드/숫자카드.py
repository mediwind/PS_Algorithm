def check(a, b):
    if a == '0':
        return False
    
    res = int(a) * 10 + int(b)
    if 1 <= res <= 34:
        return True
    
    return False


s = input()
n = len(s)
dy = [0 for _ in range(n + 1)]
dy[0] = dy[1] = 1
for i in range(1, n):
    dy[i + 1] = dy[i]
    if check(s[i - 1], s[i]):
        dy[i + 1] += dy[i - 1]
    if s[i] == '0':
        dy[i + 1] -= dy[i]

print(dy[n])