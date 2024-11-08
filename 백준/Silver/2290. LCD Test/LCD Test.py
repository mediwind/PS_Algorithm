HORIZONTAL, VERTICAL = '-', '|'
size, number = input().split()
size = int(size)


def create_segment(digit):
    segment = [[' ']*(size+2) for _ in range(2*size + 3)]
    for i in range(1, size+1):
        if digit in '02356789':
            segment[0][i] = HORIZONTAL  # a
        if digit in '01234789':
            segment[i][-1] = VERTICAL  # b
        if digit in '013456789':
            segment[size+1+i][-1] = VERTICAL  # c
        if digit in '0235689':
            segment[2*size + 2][i] = HORIZONTAL  # d
        if digit in '0268':
            segment[size+1+i][0] = VERTICAL  # e
        if digit in '045689':
            segment[i][0] = VERTICAL  # f
        if digit in '2345689':
            segment[size+1][i] = HORIZONTAL  # g
    
    return segment


lcd_display = [create_segment(digit) for digit in number]

for line in zip(*lcd_display):
    for row in line:
        print(''.join(row), end=' ')
    print()