string=input()

if len(set(string)) == 1:
    print(-1)
else:
    lt = 0
    rt = len(string) - 1

    while lt <= rt:
        if string[lt] != string[rt]:
            print(len(string))
            break
        lt += 1
        rt -= 1
    
    if lt > rt:
        print(len(string) - 1)