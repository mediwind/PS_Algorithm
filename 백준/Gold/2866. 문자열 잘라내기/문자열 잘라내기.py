r, c = map(int, input().split())
words = [input() for _ in range(r)]

cnt = 0
lt, rt = 0, r - 1
while lt <= rt:
    mid = (lt + rt) // 2
    
    flag = True
    dictionary = dict()
    for j in range(c):
        tmp = ''
        for i in range(mid, r):
            tmp += str(words[i][j])

        if tmp not in dictionary:
            dictionary[tmp] = 1
        else:
            flag = False
            break
    
    if flag:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)