import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

N = int(input())
K = int(input())

path = []

def dfs(count, current_sum, last_val):
    if count == K:
        if current_sum == N:
            print(path[0], end='')
            for x in path[1:]:
                if x >= 0:
                    print(f"+{x}", end='')
                else:
                    print(x, end='')
            print()
        return

    remain = K - count

    max_possible_add = (remain * last_val) + (remain * (remain + 1)) // 2

    min_possible_add = (remain * last_val) - (remain * (remain + 1)) // 2

    if current_sum + max_possible_add < N:
        return

    if current_sum + min_possible_add > N:
        return

    for diff in [-1, 0, 1]:
        next_val = last_val + diff
        path.append(next_val)
        dfs(count + 1, current_sum + next_val, next_val)
        path.pop()

for start_val in range(-50, 51):
    path.append(start_val)
    dfs(1, start_val, start_val)
    path.pop()