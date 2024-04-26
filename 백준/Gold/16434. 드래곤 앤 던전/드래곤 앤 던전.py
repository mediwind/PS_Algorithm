from math import ceil

import sys
input = sys.stdin.readline


def check(attk, max_hp):
    curr_hp = max_hp
    for t, a, h in rooms:
        if t == 1:
            turn = h//attk if not h%attk else h//attk + 1
            curr_hp -= a * (turn - 1)
        else:
            attk += a
            curr_hp += h
            if curr_hp > max_hp:
                curr_hp = max_hp
        
        if curr_hp <= 0:
            return False
    
    return True


n, attk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]

lt, rt = 1, n*(1_000_000**2)
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if check(attk, mid):
        rt = mid - 1
        ans = mid
    else:
        lt = mid + 1

print(ans)
