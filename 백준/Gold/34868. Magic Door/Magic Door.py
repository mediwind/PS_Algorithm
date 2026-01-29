import sys
input = sys.stdin.readline


def apply_gravity(current_grid, current_active):
    new_grid = [[EMPTY] * N for _ in range(M)]
    new_active = set()

    for c in range(N):
        items = []
        for r in range(M):
            if current_grid[r][c] != EMPTY:
                items.append((current_grid[r][c], r))

        write_r = M - 1
        for val, old_r in reversed(items):
            new_grid[write_r][c] = val

            if val == BOMB:
                if (old_r, c) in current_active:
                    new_active.add((write_r, c))
                elif write_r > old_r:
                    new_active.add((write_r, c))

            write_r -= 1

    return new_grid, new_active


def find_matches(current_grid):
    matched = set()
    for r in range(M):
        for c in range(N - 2):
            val = current_grid[r][c]
            if val > 0:
                if val == current_grid[r][c+1] == current_grid[r][c+2]:
                    matched.add((r, c))
                    matched.add((r, c+1))
                    matched.add((r, c+2))

    for c in range(N):
        for r in range(M - 2):
            val = current_grid[r][c]
            if val > 0:
                if val == current_grid[r+1][c] == current_grid[r+2][c]:
                    matched.add((r, c))
                    matched.add((r+1, c))
                    matched.add((r+2, c))
    return matched


def explode_bombs(current_grid, bombs_to_explode):
    destroyed = set()
    for r, c in bombs_to_explode:
        destroyed.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            while 0 <= nr < M and 0 <= nc < N:
                val = current_grid[nr][nc]
                if val == VIBRANIUM:
                    break
                if val != EMPTY:
                    destroyed.add((nr, nc))
                nr += dr
                nc += dc
    return destroyed


VIBRANIUM = -1
BOMB = 0
EMPTY = -2

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
r1, c1, r2, c2 = map(int, input().split())

r1 -= 1; c1 -= 1
r2 -= 1; c2 -= 1

grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]

total_destroyed = 0
activated_bombs = set()


while True:
    stage1_occurred = False
    while True:
        matches = find_matches(grid)

        if not matches:
            break

        stage1_occurred = True

        count = 0
        for r, c in matches:
            if grid[r][c] != EMPTY:
                grid[r][c] = EMPTY
                count += 1
        total_destroyed += count

        grid, activated_bombs = apply_gravity(grid, activated_bombs)

    if not activated_bombs:
        if not stage1_occurred: 
            break

        if not activated_bombs: 
            break

    targets = explode_bombs(grid, activated_bombs)

    count = 0
    for r, c in targets:
        if grid[r][c] != EMPTY:
            grid[r][c] = EMPTY
            count += 1
    total_destroyed += count

    activated_bombs = set()

    grid, activated_bombs = apply_gravity(grid, activated_bombs)

print(total_destroyed)