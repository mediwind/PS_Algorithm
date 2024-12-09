import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
words.sort(key = len)

res = 0
for i in range(n):
    is_prefix = False
    word1 = words[i]
    for j in range(i + 1, n):
        word2 = words[j]
        if word1 == word2[:len(word1)]:
            is_prefix = True
            break
    
    if not is_prefix:
        res += 1

print(res)