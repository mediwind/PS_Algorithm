from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
flight_scores = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    if a < b:
        flight_scores[a][b] = max(flight_scores[a][b], c)

# dy[k][city]는 k개의 도시를 거쳐 city에 도착했을 때 최대 점수
dy = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

for num_cities_visited in range(2, M + 1):
    for end_city in range(N + 1):
        for start_city in range(1, end_city):
            if flight_scores[start_city][end_city] > 0:
                if start_city == 1: # 첫비행
                    current_path_score = flight_scores[start_city][end_city]
                    dy[num_cities_visited][end_city] = max(dy[num_cities_visited][end_city], current_path_score)
                elif dy[num_cities_visited - 1][start_city] > 0: # 이전 경로가 존재
                    current_path_score = dy[num_cities_visited - 1][start_city] + flight_scores[start_city][end_city]
                    dy[num_cities_visited][end_city] = max(dy[num_cities_visited][end_city], current_path_score)

max_total_score = 0
for k_cities in range(1, M + 1):
    max_total_score = max(max_total_score, dy[k_cities][N])

print(max_total_score)