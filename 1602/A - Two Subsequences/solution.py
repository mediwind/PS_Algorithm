import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().rstrip()
    sorted_s = sorted(s)
 
    a = sorted_s[0]
    b = ''
 
    cnt = 0
    for c in s:
        if c == a and cnt == 0:
            cnt += 1
        else:
            b += c
            
    print(a, b)