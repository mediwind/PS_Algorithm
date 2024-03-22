n, k = map(int, input().split())

if k >= n:
    print(0)
else:
    answer = 0

    while True:
        cnt = 0
        temp = n
#         print('1:', answer, temp, cnt)
        while temp > 0:
            if temp % 2 == 0:
                temp //= 2
            else:
                temp //= 2
                cnt += 1
#             print('2:', answer, temp, cnt)

        if k >= cnt:
#             print('3:', answer, temp, cnt)
            break

        n += 1
        answer += 1

    print(answer)