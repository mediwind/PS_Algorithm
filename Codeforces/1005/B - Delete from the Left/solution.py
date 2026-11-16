import sys
input = sys.stdin.readline
 
s = input().strip()
t = input().strip()
 
i = len(s) - 1
j = len(t) - 1
common_len = 0
 
while i >= 0 and j >= 0 and s[i] == t[j]:
    common_len += 1
    i -= 1
    j -= 1
 
ans = len(s) + len(t) - 2 * common_len
print(ans)