import sys
input = sys.stdin.readline


# 사다리 정보를 위쪽/아래쪽으로 분리하여 반환
def parse_ladder():
    found = False
    up, down = list(), list()
    for _ in range(N):
        row = input().strip()
        if row[0] == '?':
            found = True
        elif not found:
            up.append(row)
        else:
            down.append(row)
    down.reverse()
    return up, down


# 주어진 사다리 정보를 따라 참가자 순서를 시뮬레이션
def simulate(state, ladder):
    for row in ladder:
        for i in range(K - 1):
            if row[i] == '-':
                state[i], state[i + 1] = state[i + 1], state[i]

                
# 숨겨진 줄(가로줄)을 완성하거나 불가능하면 x로 채워 반환
def get_hidden_row(before, after):
    res = list()
    for i in range(K-1):
        if before[i] == after[i + 1] and before[i + 1] == after[i]:
            res.append('-')
        else:
            res.append('*')
    temp = before.copy()
    simulate(temp, ["".join(res)])
    return "".join(res) if temp == after else 'x' * (K - 1)


K = int(input())
N = int(input())

start = [chr(ord('A') + i) for i in range(K)]
goal = list(input().strip())

up, down = parse_ladder()
simulate(start, up)
simulate(goal, down)
print(get_hidden_row(start, goal))