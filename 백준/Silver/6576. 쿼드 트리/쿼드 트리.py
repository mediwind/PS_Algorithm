import sys

MAX_N = 1024
xbm = [[0 for _ in range(MAX_N // 8)] for _ in range(MAX_N)]


def quadtree(top, left, size, input_stream):
    char = input_stream.read(1)
    if char == 'W':
        for i in range(top, top + size):
            for j in range(left, left + size):
                xbm[i][j // 8] &= ~(1 << (j % 8))
    elif char == 'B':
        for i in range(top, top + size):
            for j in range(left, left + size):
                xbm[i][j // 8] |= 1 << (j % 8)
    elif char == 'Q':
        quadtree(top, left, size // 2, input_stream)
        quadtree(top, left + size // 2, size // 2, input_stream)
        quadtree(top + size // 2, left, size // 2, input_stream)
        quadtree(top + size // 2, left + size // 2, size // 2, input_stream)


input_stream = sys.stdin
n = int(input_stream.readline())
quadtree(0, 0, n, input_stream)
print("#define quadtree_width %d" % n)
print("#define quadtree_height %d" % n)
print("static char quadtree_bits[] = {")
for i in range(n):
    for j in range(n // 8):
        print("0x%02x," % xbm[i][j], end='')
    print()
print("};")