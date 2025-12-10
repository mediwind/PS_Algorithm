rows = []
for _ in range(10):
    parts = []
    while len(parts) < 10:
        parts.extend(map(int, input().split()))
    rows.extend(parts[:10])

last_row = last_col = 0
for i, v in enumerate(rows[:100]):
    if v == 100:
        last_row, last_col = divmod(i, 10)
        break

board = ["####.###.#", "###.##.##.", "##.#.#....", ".........."]

i = 0
out = []
for row in range(10):
    if row == last_row:
        row_str = board[3][:last_col] + '#' + board[3][last_col+1:]
        out.append(row_str)
    elif (row - last_row) % 2 == 0:
        out.append(board[i])
        i += 1
    else:
        out.append(board[3])

for line in out:
    print(line)