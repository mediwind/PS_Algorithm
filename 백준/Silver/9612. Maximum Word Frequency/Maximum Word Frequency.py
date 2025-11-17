import sys
input = sys.stdin.readline

n = int(input().rstrip())
counter = dict()
maxi = 0
for _ in range(n):
    word = input().rstrip()
    counter[word] = counter.get(word, 0) + 1
    if counter[word] >= maxi:
        maxi = counter[word]

for word in sorted(counter, reverse = True):
    cnt = counter[word]
    if cnt == maxi:
        print(word, cnt)
        break