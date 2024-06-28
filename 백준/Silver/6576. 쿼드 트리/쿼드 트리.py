import sys

MAX_N = 1024
# 이미지 데이터를 저장하는 2차원 배열입니다. 비트 연산을 통해 흑/백을 저장합니다.
xbm = [[0 for _ in range(MAX_N // 8)] for _ in range(MAX_N)]


def quadtree(top, left, size, input_stream):
    # 입력 문자열에서 문자를 하나 읽습니다.
    char = input_stream.read(1)
    if char == 'W':
        # 해당 영역을 흰색으로 채웁니다.
        for i in range(top, top + size):
            for j in range(left, left + size):
                xbm[i][j // 8] &= ~(1 << (j % 8))
    elif char == 'B':
        # 해당 영역을 검은색으로 채웁니다.
        for i in range(top, top + size):
            for j in range(left, left + size):
                xbm[i][j // 8] |= 1 << (j % 8)
    elif char == 'Q':
        # 해당 영역을 4개의 작은 영역으로 나누고, 각각에 대해 재귀적으로 함수를 호출합니다.
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