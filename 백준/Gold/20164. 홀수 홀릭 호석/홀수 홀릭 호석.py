def counting_odd_number(word):
    cnt = 0
    
    for w in word:
        if int(w) % 2:
            cnt += 1
    
    return cnt


def DFS(number, odd_count):
    global mini, maxi
    
    if len(number) == 1:
        mini = min(mini, odd_count)
        maxi = max(maxi, odd_count)
    elif len(number) == 2:
        temp = str(int(number[0]) + int(number[1]))
        DFS(temp, odd_count + counting_odd_number(temp))
    else:
        for i in range(len(number) - 2):
            for j in range(i + 1, len(number) - 1):
                a = number[:i + 1]
                b = number[i + 1:j + 1]
                c = number[j + 1:]

                temp = str(int(a) + int(b) + int(c))
                
                DFS(temp, odd_count + counting_odd_number(temp))


n = input()

mini = float("inf")
maxi = float("-inf")

DFS(n, counting_odd_number(n))
print(mini, maxi)