from collections import defaultdict

import sys
input = sys.stdin.readline

states = defaultdict(dict)
N = int(input())
for _ in range(N):
    city, state = input().split()
    states[state][city[:2]] = states[state].get(city[:2], 0) + 1

cnt = 0
for k in states.keys():
    for v in states[k]:
        if v == k: # "Fl"OWER "FL"과 같은 경우도 계산에 포함하면 X
            continue
        if v in states and k in states[v]:
            cnt += states[k][v] * states[v][k]

print(cnt // 2)