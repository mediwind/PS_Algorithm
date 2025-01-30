from itertools import product


def check(arr):
    max_length = 1
    length = 1
    for i in range(n - 1):
        if arr[i] != arr[i + 1]:
            length += 1
            max_length = max(max_length, length)
            if max_length > m:
                return False
        else:
            length = 1
            
    return max_length == m


n, m = map(int, input().split())
stations = [input() for _ in range(n)]
ans = 0
for pro in product([0, 1], repeat = n):
    if check(pro):
        res = 1
        for pr in pro:
            if pr:
                res *= 5
            else:
                res *= 11
        ans += res
        
print(ans % (10 ** 9 + 7))