import sys
input = sys.stdin.readline

def bit_iter(x: int):
    while x:
        lsb = x & -x
        yield lsb.bit_length() - 1
        x -= lsb

def solve_case(m: int, n: int, k: int, tiles, board):
    cell_id = {}
    id_cell = []
    for r in range(m):
        for c in range(n):
            if board[r][c] is not None:
                cell_id[(r, c)] = len(id_cell)
                id_cell.append((r, c))

    free_cells = len(id_cell)
    if free_cells != 2 * k:
        return None

    tile_index = {}
    for i, (a, b) in enumerate(tiles):
        key = (a, b) if a <= b else (b, a)
        tile_index[key] = i

    col_count = free_cells + k
    row_masks = []
    row_info = []

    def add_row(r1, c1, r2, c2, tile_i, orient):
        cidx1 = cell_id[(r1, c1)]
        cidx2 = cell_id[(r2, c2)]
        tidx = free_cells + tile_i
        mask = (1 << cidx1) | (1 << cidx2) | (1 << tidx)
        row_info.append((r1, c1, r2, c2, orient))
        row_masks.append(mask)

    for r in range(m):
        for c in range(n):
            if board[r][c] is None:
                continue
            d1 = board[r][c]
            if c + 1 < n and board[r][c + 1] is not None:
                d2 = board[r][c + 1]
                key = (d1, d2) if d1 <= d2 else (d2, d1)
                ti = tile_index.get(key)
                if ti is not None:
                    add_row(r, c, r, c + 1, ti, 'H')
            if r + 1 < m and board[r + 1][c] is not None:
                d2 = board[r + 1][c]
                key = (d1, d2) if d1 <= d2 else (d2, d1)
                ti = tile_index.get(key)
                if ti is not None:
                    add_row(r, c, r + 1, c, ti, 'V')

    row_count = len(row_masks)
    if row_count == 0 and col_count > 0:
        return None

    col_rows = [0] * col_count
    for r_idx, mask in enumerate(row_masks):
        mm = mask
        while mm:
            lsb = mm & -mm
            c_idx = lsb.bit_length() - 1
            col_rows[c_idx] |= (1 << r_idx)
            mm -= lsb

    all_cols_mask = (1 << col_count) - 1
    all_rows_mask = (1 << row_count) - 1

    for c_idx in range(col_count):
        if col_rows[c_idx] == 0:
            return None

    first_solution = None
    total_solutions = 0
    partial = []

    def choose_column(active_cols: int, active_rows: int):
        best_c = -1
        best_cnt = 10**9
        for c in bit_iter(active_cols):
            cnt = (col_rows[c] & active_rows).bit_count()
            if cnt < best_cnt:
                best_cnt = cnt
                best_c = c
                if best_cnt <= 1:
                    break
        return best_c, best_cnt

    def dfs(active_cols: int, active_rows: int):
        nonlocal first_solution, total_solutions
        if active_cols == 0:
            total_solutions += 1
            if first_solution is None:
                first_solution = partial.copy()
            return
        c, cnt = choose_column(active_cols, active_rows)
        if cnt == 0:
            return
        candidates = col_rows[c] & active_rows
        while candidates:
            lsb = candidates & -candidates
            r_idx = lsb.bit_length() - 1
            candidates -= lsb
            row_mask = row_masks[r_idx]
            covered_cols = row_mask & active_cols
            new_active_cols = active_cols & ~covered_cols
            conflict_rows = 0
            mm = covered_cols
            while mm:
                lsb2 = mm & -mm
                c2 = lsb2.bit_length() - 1
                conflict_rows |= col_rows[c2]
                mm -= lsb2
            new_active_rows = active_rows & ~conflict_rows
            partial.append(r_idx)
            dfs(new_active_cols, new_active_rows)
            partial.pop()

    dfs(all_cols_mask, all_rows_mask)

    if total_solutions == 0:
        return None

    out = [['X' if board[r][c] is None else '.' for c in range(n)] for r in range(m)]
    for r_idx in first_solution:
        r1, c1, r2, c2, orient = row_info[r_idx]
        if orient == 'H':
            if c1 < c2:
                out[r1][c1] = '['
                out[r2][c2] = ']'
            else:
                out[r2][c2] = '['
                out[r1][c1] = ']'
        else:
            if r1 < r2:
                out[r1][c1] = 'n'
                out[r2][c2] = 'u'
            else:
                out[r2][c2] = 'n'
                out[r1][c1] = 'u'

    return out, total_solutions - 1

def read_ints_needed(count):
    res = []
    while len(res) < count:
        line = input().strip()
        if not line:
            continue
        parts = line.strip().split()
        if not parts:
            continue
        for p in parts:
            res.append(p)
            if len(res) >= count:
                break
    return list(map(int, res[:count]))

results = []
while True:
    line = input().strip()
    if not line:
        continue
    parts = line.strip().split()
    if not parts:
        continue
    m, n, k = map(int, parts)
    if m == 0 and n == 0 and k == 0:
        break
    
    tiles_flat = read_ints_needed(2 * k) if k > 0 else []
    tiles = []
    for i in range(0, len(tiles_flat), 2):
        tiles.append((tiles_flat[i], tiles_flat[i + 1]))
    board = []
    for _ in range(m):
        row_parts = []
        while True:
            line2 = input().strip()
            if not line2:
                continue
            parts2 = line2.strip().split()
            if parts2:
                row_parts = parts2
                break
        row = []
        for tok in row_parts:
            if tok == 'X':
                row.append(None)
            else:
                row.append(int(tok))
        board.append(row)
    solved = solve_case(m, n, k, tiles, board)
    if solved is None:
        print("impossible")
        print()
    else:
        out_grid, other_count = solved
        for r in range(m):
            print("".join(out_grid[r]))
        print(other_count)
        print()