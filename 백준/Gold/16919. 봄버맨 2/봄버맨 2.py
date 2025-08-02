import sys


input = sys.stdin.readline


def bomberman_simulation(rows, cols, time):

    grid = [list(input().rstrip()) for _ in range(rows)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def detonate(board):

        result = [['O'] * cols for _ in range(rows)]

        for x in range(rows):

            for y in range(cols):

                if board[x][y] == 'O':

                    result[x][y] = '.'

                    for dx, dy in directions:

                        nx, ny = x + dx, y + dy

                        if 0 <= nx < rows and 0 <= ny < cols:

                            result[nx][ny] = '.'

        return result


    if time == 1:

        for row in grid:

            print(''.join(row))

    elif time % 2 == 0:

        for _ in range(rows):

            print('O' * cols)

    elif time % 4 == 3:

        exploded = detonate(grid)

        for row in exploded:

            print(''.join(row))

    elif time % 4 == 1:

        first = detonate(grid)

        second = detonate(first)

        for row in second:

            print(''.join(row))


if __name__ == "__main__":

    R, C, N = map(int, input().split())

    bomberman_simulation(R, C, N)