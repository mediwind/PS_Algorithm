import math
import sys
input = sys.stdin.readline

N, Hatk = map(int, input().split())
HcurHP = HmaxHP = dmg = 0

for _ in range(N):
    t, a, h = map(int, input().split())
    
    if t == 1:
        dmg = ((math.ceil(h / Hatk) - 1) * a)
        
        if HcurHP >= dmg:
            HcurHP -= dmg
        else:
            HmaxHP += dmg - HcurHP
            HcurHP = 0
    else:
        Hatk += a
        HcurHP = min(HcurHP + h, HmaxHP)

print(HmaxHP + 1)