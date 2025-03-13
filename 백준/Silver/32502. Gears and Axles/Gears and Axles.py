import math
import sys
input = sys.stdin.readline

n = int(input().rstrip())

gears = [None for _ in range(100000)]

for _ in range(n):
    s, c = map(int, input().rstrip().split())
    s -= 1

    if gears[s] is None:
        gears[s] = list()
    gears[s].append(math.log(c))

angular = 0.0

for gear in gears:
    if gear is not None:
        gear.sort()
        size = len(gear)
        for i in range(size // 2):
            angular += gear[size - i - 1] - gear[i]

print(angular)