import sys
input = sys.stdin.readline

# 입력을 받습니다.
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 각 열에 대해 소와 빈 칸이 번갈아 나타나는 두 가지 배치에 대한 아름다움의 합을 계산합니다.
vertical_answer = 0
for x in range(n):
    sums = [0, 0]
    for y in range(n):
        # y % 2는 y가 짝수일 때 0, 홀수일 때 1입니다. 이를 통해 소와 빈 칸이 번갈아 나타나게 합니다.
        sums[y % 2] += grid[x][y]
    # 두 배치 중에서 아름다움이 더 큰 것을 선택합니다.
    vertical_answer += max(sums)

# 같은 과정을 각 행에 대해 수행합니다.
horizontal_answer = 0
for y in range(n):
    sums = [0, 0]
    for x in range(n):
        # x % 2는 x가 짝수일 때 0, 홀수일 때 1입니다. 이를 통해 소와 빈 칸이 번갈아 나타나게 합니다.
        sums[x % 2] += grid[x][y]
    # 두 배치 중에서 아름다움이 더 큰 것을 선택합니다.
    horizontal_answer += max(sums)

# 행과 열 배치에서 얻은 최대 아름다움 중 더 큰 값을 출력합니다.
print(max(horizontal_answer, vertical_answer))