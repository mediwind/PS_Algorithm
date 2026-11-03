import sys
input = sys.stdin.readline
 
n = int(input().strip())
s = input().strip()
 
count_0 = s.count('0')
count_1 = n - count_0
 
print(abs(count_0 - count_1))