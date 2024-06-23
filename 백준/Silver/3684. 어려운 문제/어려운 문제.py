def calculating(x, a, b):
    return (a * x + b) % 10001


def finding():
    for a in range(10001):
        for b in range(10001):
            cnt = 0
            for i in range(t - 1):
                num = calculating(arr[i], a, b)
                if arr[i + 1] == calculating(num, a, b):
                    cnt += 1
                else:
                    break

            if cnt == t - 1:
                return a, b

    return None, None


t = int(input())
arr = [int(input()) for _ in range(t)]

a, b = finding()
for i in range(t):
    print(calculating(arr[i], a, b))