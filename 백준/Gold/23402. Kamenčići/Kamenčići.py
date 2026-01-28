import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def get_b(L, R, a):
    current_reds = prefix_reds[R+1] - prefix_reds[L]
    removed_reds = total_reds - current_reds
    return removed_reds - a


def game(L, R, a):
    b = get_b(L, R, a)

    if a == K:
        return False
    if b == K:
        return True
    if L > R:
        return True

    state = (L, R, a)
    if state in memo:
        return memo[state]

    turns_played = N - (R - L + 1)

    res = False

    left_val = 1 if S[L] == 'C' else 0
    right_val = 1 if S[R] == 'C' else 0

    if turns_played % 2 == 0: 
        if game(L + 1, R, a + left_val):
            res = True
        elif game(L, R - 1, a + right_val):
            res = True
        else:
            res = False
    else:
        can_win_left = game(L + 1, R, a)
        can_win_right = game(L, R - 1, a)

        if can_win_left and can_win_right:
            res = True
        else:
            res = False

    memo[state] = res
    return res


N, K = map(int, input().split())
S = input().strip()

prefix_reds = [0] * (N + 1)
for i in range(N):
    prefix_reds[i+1] = prefix_reds[i] + (1 if S[i] == 'C' else 0)

total_reds = prefix_reds[N]

memo = {}

if game(0, N - 1, 0):
    print("DA")
else:
    print("NE")