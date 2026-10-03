import sys
input = sys.stdin.readline
 
s = input().strip()
 
words = s.replace("WUB", " ").split()
 
print(*words)