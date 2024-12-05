from collections import deque


def button_a(x):
    return x + 1


def button_b(x):
    x *= 2
    if x >= 99999:
        return x
    
    string = list(str(x))
    res = ""
    
    changed = False
    for s in string:
        if not changed and s != "0":
            changed = True
            res += str(int(s) - 1)
            continue
        res += s
    
    return int(''.join(res))


n, t, g = map(int, input().split())
Q = deque([(n, 0)])
ch = {n}

while Q:
    x, dist = Q.popleft()
    
    if x == g and dist <= t:
        print(dist)
        break
    elif x == g and dist > t:
        print("ANG")
        break
    
    res_a = button_a(x)
    res_b = button_b(x)
    
    if res_a not in ch:
        if res_a > 99999:
            continue
        ch.add(res_a)
        Q.append((res_a, dist + 1))
    if res_b not in ch:
        if res_b > 99999:
            continue
        ch.add(res_b)
        Q.append((res_b, dist + 1))
else:
    print("ANG")