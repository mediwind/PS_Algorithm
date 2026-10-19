import sys
input = sys.stdin.readline
 
n = int(input())
s = input().strip()
 
counts = {}
best_gram = ""
max_count = 0
 
for i in range(n - 1):
    two_gram = s[i:i+2]
    counts[two_gram] = counts.get(two_gram, 0) + 1
    
    if counts[two_gram] > max_count:
        max_count = counts[two_gram]
        best_gram = two_gram
 
print(best_gram)