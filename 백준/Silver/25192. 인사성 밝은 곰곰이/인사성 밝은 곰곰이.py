import sys
input = sys.stdin.readline

n = int(input().rstrip())

ans = 0
ch = set()
for _ in range(n):
    s = input().rstrip()
    
    if s == "ENTER":
        ch = set()
    else:
        if s not in ch:
            ch.add(s)
            ans += 1

print(ans)