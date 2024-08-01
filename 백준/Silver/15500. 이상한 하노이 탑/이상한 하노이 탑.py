from collections import deque

# 입력 받기
N = int(input())
disks = list(map(int, input().split()))

# 각 장대를 나타내는 스택
source = deque(disks)
auxiliary = deque()
destination = deque()

# 이동 횟수와 목표 디스크 번호 초기화
move_count = 0
target_disk = N
moves = []

while True:
    # 모든 디스크가 목적지 장대에 쌓이면 종료
    if len(destination) == N:
        break

    # 소스 장대에서 디스크를 옮기는 과정
    while source:
        disk = source.pop()
        move_count += 1

        if disk == target_disk:
            destination.append(disk)
            target_disk -= 1
            moves.append("1 3")
            if target_disk == 0:
                break
        else:
            auxiliary.append(disk)
            moves.append("1 2")

    # 보조 장대에서 디스크를 옮기는 과정
    while auxiliary:
        disk = auxiliary.pop()
        move_count += 1

        if disk == target_disk:
            destination.append(disk)
            target_disk -= 1
            moves.append("2 3")
            if target_disk == 0:
                break
        else:
            source.append(disk)
            moves.append("2 1")

# 결과 출력
print(move_count)
for order in moves:
    print(order)