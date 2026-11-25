import sys
from math import comb

input = sys.stdin.readline

A = int(input()) / 100
B = int(input()) / 100

scores = [2, 3, 5, 7, 11, 13, 17]

A_pro, B_pro = 0, 0
for score in scores:
    A_pro += comb(18, score) * (A ** score) * ((1 - A) ** (18 - score))
    B_pro += comb(18, score) * (B ** score) * ((1 - B) ** (18 - score))

ans = 1 - ((1 - A_pro) * (1 - B_pro))
print(ans)