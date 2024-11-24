from collections import Counter

s = input()
n = len(s)
count = Counter(s)
s *= 2
a_count = s[:count['a']].count('a')
b_count = s[:count['a']].count('b')
ans = float('inf')
for i in range(1, len(s) // 2 + 1):
    if s[i - 1] == 'a':
        a_count -= 1
    else:
        b_count -= 1
        
    if s[i + count['a'] - 1] == 'a':
        a_count += 1
    else:
        b_count += 1
    
    ans = min(ans, b_count)

print(ans)