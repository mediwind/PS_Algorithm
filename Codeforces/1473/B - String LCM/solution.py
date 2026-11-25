import sys
from math import lcm
 
input = sys.stdin.readline
 
q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    
    len_s, len_t = len(s), len(t)
    lcm_len = lcm(len_s, len_t)
    
    cand_s = s * (lcm_len // len_s)
    cand_t = t * (lcm_len // len_t)
    
    if cand_s == cand_t:
        print(cand_s)
    else:
        print(-1)