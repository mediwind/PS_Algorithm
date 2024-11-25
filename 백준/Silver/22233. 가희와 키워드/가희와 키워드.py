import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = {input().strip() for _ in range(n)}

for _ in range(m):
    words = set(input().strip().split(','))
    keywords -= words
    print(len(keywords))