import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
current_level, current_exp, target_level = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

# 시작 위치 찾기
start_x, start_y = -1, -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == -3:
            start_x, start_y = i, j
            break

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * m for _ in range(n)]

# 최소 힙 초기화: (해당 칸에 진입하기 위해 필요한 최소 레벨, x 좌표, y 좌표)
heap = []

# 시작점은 진입 제약이 없으므로 필요 레벨 0으로 힙에 넣습니다.
heapq.heappush(heap, (0, start_x, start_y))
visited[start_x][start_y] = True

can_reach_raid = False

while heap:
    req_level, x, y = heapq.heappop(heap)
    
    # 힙에서 꺼낸 칸의 진입 필요 레벨이 현재 레벨보다 높다면
    # 남은 칸들은 더 높은 레벨을 요구하므로 더 이상 진행할 수 없습니다.
    if req_level > current_level:
        break
        
    cell = grid[x][y]
    
    # 레이드 장소에 도달했다면 탐색 성공
    # (힙에 들어갈 때 필요 레벨을 target_level로 설정했으므로, 
    # 여기까지 왔다는 것은 current_level >= target_level 임이 보장됩니다.)
    if cell == -2:
        can_reach_raid = True
        break
        
    # 몬스터인 경우 경험치 획득 및 레벨업 처리
    if cell > 0:
        current_exp += cell
        while current_exp >= current_level:
            current_exp -= current_level
            current_level += 1
            
    # 인접한 네 방향 탐색하여 힙에 추가
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and grid[nx][ny] != -1:
                visited[nx][ny] = True
                
                next_cell = grid[nx][ny]
                
                # 다음 칸의 성질에 따라 진입 필요 레벨을 계산합니다.
                if next_cell == -2:
                    next_req = target_level
                elif next_cell > 0:
                    next_req = next_cell + 1
                else:
                    next_req = 0
                    
                heapq.heappush(heap, (next_req, nx, ny))

if can_reach_raid:
    print("O")
else:
    print("X")