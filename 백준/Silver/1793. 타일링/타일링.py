import sys
input = sys.stdin.readline


MAX_N = 250
dy = [0 for _ in range(MAX_N + 1)]
dy[0] = 1

if MAX_N >= 1:
    dy[1] = 1

for n in range(2, MAX_N + 1):
    dy[n] = dy[n - 1] + 2 * dy[n - 2]

while True:
    try:
        line = input()
        if not line.strip():
            break
        n = int(line)
        print(dy[n])
    except EOFError:
        break