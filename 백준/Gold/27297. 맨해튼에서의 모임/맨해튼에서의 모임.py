import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 입력값을 저장할 리스트의 리스트를 초기화
values = [[] for _ in range(N)]

# M개의 줄을 읽어들여 각 줄에 N개의 정수를 저장
for _ in range(M):
    row = list(map(int, input().split()))
    for i in range(N):
        values[i].append(row[i])

# 총 거리와 중간값 리스트를 초기화
total_distance = 0
medians = list()

# 각 리스트를 처리하여 중간값을 찾고 총 거리를 계산
for i in range(N):
    values[i].sort()
    median = values[i][M // 2]
    medians.append(median)
    total_distance += sum(abs(x - median) for x in values[i])

# 총 거리를 출력
print(total_distance)

# 중간값들을 출력
print(' '.join(map(str, medians)))