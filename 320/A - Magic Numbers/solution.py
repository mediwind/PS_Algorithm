import sys
input = sys.stdin.readline
 
s = input().strip()
 
i = 0
n = len(s)
is_magic = True
 
while i < n:
    if s[i:i+3] == "144":
        i += 3
    elif s[i:i+2] == "14":
        i += 2
    elif s[i] == "1":
        i += 1
    else:
        is_magic = False
        break
 
if is_magic:
    print("YES")
else:
    print("NO")