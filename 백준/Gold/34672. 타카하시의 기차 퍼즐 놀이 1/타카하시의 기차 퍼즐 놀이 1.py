import sys
input = sys.stdin.readline

q = int(input().strip())
out_lines = []

pat0_top = "114"
pat0_bot = "144"
pat1_top = "322"
pat1_bot = "332"

for _ in range(q):
    r, c, k = map(int, input().split())

    if r != 2 or c % 3 != 0:
        out_lines.append("-1")
        continue

    blocks = c // 3

    if blocks <= 60:
        if k > (1 << blocks):
            out_lines.append("-1")
            continue

    x = k - 1
    top_parts = []
    bot_parts = []

    for bit_pos in range(blocks - 1, -1, -1):
        if (x >> bit_pos) & 1:
            top_parts.append(pat1_top)
            bot_parts.append(pat1_bot)
        else:
            top_parts.append(pat0_top)
            bot_parts.append(pat0_bot)

    out_lines.append("".join(top_parts))
    out_lines.append("".join(bot_parts))

print("\n".join(out_lines))