import sys
input = sys.stdin.readline

def set_winner(games_a: int, games_b: int, tie_break_allowed: bool):
    if games_a == games_b:
        return None

    if tie_break_allowed:
        if games_a == 7 and games_b == 6:
            return 0
        if games_a == 6 and games_b == 7:
            return 1
        if games_a == 7 and games_b == 5:
            return 0
        if games_a == 5 and games_b == 7:
            return 1
        if games_a == 6 and 0 <= games_b <= 4:
            return 0
        if games_b == 6 and 0 <= games_a <= 4:
            return 1
        return None

    if games_a > games_b:
        winner = 0
        w, l = games_a, games_b
    else:
        winner = 1
        w, l = games_b, games_a

    if w == 6:
        return winner if l <= 4 else None
    if w >= 7:
        return winner if w == l + 2 else None
    return None


name_a, name_b = input().split()
match_count = int(input().strip())

federer_side = None
if name_a == "federer":
    federer_side = 0
elif name_b == "federer":
    federer_side = 1

for _ in range(match_count):
    line = input().strip()
    while line == "":
        line = input().strip()

    set_tokens = line.split()
    sets_won = [0, 0]
    ok = True

    for set_idx, token in enumerate(set_tokens):
        if sets_won[0] == 2 or sets_won[1] == 2:
            ok = False
            break

        if ":" not in token:
            ok = False
            break

        left, right = token.split(":", 1)
        try:
            games_a = int(left)
            games_b = int(right)
        except ValueError:
            ok = False
            break

        winner = set_winner(games_a, games_b, tie_break_allowed=(set_idx < 2))
        if winner is None:
            ok = False
            break

        if federer_side is not None and winner != federer_side:
            ok = False
            break

        sets_won[winner] += 1

    if ok and sets_won[0] != 2 and sets_won[1] != 2:
        ok = False

    print("da" if ok else "ne")