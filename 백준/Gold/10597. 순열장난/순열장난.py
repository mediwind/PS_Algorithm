import sys


def DFS(index):
    if index == len(word):
        print(' '.join(answer))
        sys.exit(0)
        
    if word[index] != '0' and not ch[int(word[index])]:
        answer.append(word[index])
        ch[int(word[index])] = 1
        DFS(index + 1)
        answer.pop()
        ch[int(word[index])] = 0

    if word[index] != '0':
        if int(word[index: index + 2]) <= n:
            if not ch[int(word[index:index + 2])]:
                answer.append(word[index:index + 2])
                ch[int(word[index:index + 2])] = 1
                DFS(index + 2)
                answer.pop()
                ch[int(word[index:index + 2])] = 0


word = input().rstrip()

if len(word) <= 9:
    n = len(word)
else:
    n = 9 + (len(word) - 9) // 2

answer = list()
ch = [0 for _ in range(n + 1)]

DFS(0)