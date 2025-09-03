import sys
sys.setrecursionlimit(10 ** 5)
MOD = 1_000_000


def calculate_powers_of_two(n):  # 2의 거듭제곱을 미리 계산하여 저장
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        powers[i] = (powers[i - 1] * 2) % MOD
    return powers


def hanoi(disc, target, positions, powers):  # 하노이 탑 최소 이동 계산
    global moves
    if disc == 0:
        return

    current = positions[disc]
    auxiliary = 6 - current - target

    if current == target:
        hanoi(disc - 1, target, positions, powers)
    else:
        moves = (moves + powers[disc - 1]) % MOD
        hanoi(disc - 1, auxiliary, positions, powers)


n = int(input())
powers = calculate_powers_of_two(n)

pole1, pole2, pole3 = map(int, input().split())

# 디스크 위치 기록
positions = [0 for _ in range(n + 1)]
if pole1 > 0:
    for x in map(int, input().split()):
        positions[x] = 1
if pole2 > 0:
    for x in map(int, input().split()):
        positions[x] = 2
if pole3 > 0:
    for x in map(int, input().split()):
        positions[x] = 3

moves = 0
hanoi(n, positions[n], positions, powers)

print(positions[n])
print(moves)