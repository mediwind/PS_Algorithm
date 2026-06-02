import sys
input = sys.stdin.readline
 
n, q = map(int, input().split())
s = input().rstrip()
 
prefix_sum = [0] * (n + 1)
 
for i in range(n):
    char_value = ord(s[i]) - ord('a') + 1
    prefix_sum[i + 1] = prefix_sum[i] + char_value
 
for _ in range(q):
    l, r = map(int, input().split())
    
    ans = prefix_sum[r] - prefix_sum[l - 1]
    print(ans)