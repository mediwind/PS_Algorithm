def counting(number, x):
    cnt = 0
    for i in range(2, -1, -1):
        cnt += (number // (10**i)) * (x**i)
        number %= 10**i
    
    return cnt


t = int(input())
answers = list()
for _ in range(t):
    a, b = map(int, input().split())

    # Initialize both bases at 10. Increment the base that produces the
    # smaller evaluated result until they yield an equal result.
    x = y = 10
    while x <= 15000 and y <= 15000:
        num_x = counting(a, x)
        num_y = counting(b, y)
#         print(x, y, num_x, num_y)
        if num_x < num_y:
            x += 1
        elif num_x > num_y:
            y += 1
        else:
            print(x, y)
            break