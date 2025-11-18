import sys
input = sys.stdin.readline

n = int(input().rstrip())
rainbow = {"ChongChong"}
for _ in range(n):
    a, b = input().rstrip().split()
    if a in rainbow or b in rainbow:
        rainbow.add(a)
        rainbow.add(b)

print(len(rainbow))