import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    try:
        line = sys.stdin.readline()
        if not line: break
        n = int(line.strip())
        if n == 0:
            break
    except ValueError:
        break

    a, b, d = map(int, sys.stdin.readline().split())

    obstacles = set()
    
    obs_min_x, obs_max_x = 1000, -1000
    obs_min_y, obs_max_y = 1000, -1000

    for _ in range(n):
        ox, oy = map(int, sys.stdin.readline().split())
        obstacles.add((ox, oy))
        obs_min_x = min(obs_min_x, ox)
        obs_max_x = max(obs_max_x, ox)
        obs_min_y = min(obs_min_y, oy)
        obs_max_y = max(obs_max_y, oy)

    x, y = a, b
    direction = 0
    step = 0

    visited = {}

    while step < d:
        escaped = False
        if direction == 0 and x > obs_max_x:
            escaped = True
        elif direction == 2 and x < obs_min_x:
            escaped = True
        elif direction == 1 and y > obs_max_y:
            escaped = True
        elif direction == 3 and y < obs_min_y:
            escaped = True

        if escaped:
            remain = d - step
            x += dx[direction] * remain
            y += dy[direction] * remain
            break

        state = (x, y, direction)

        if state in visited:
            prev_step = visited[state]
            cycle_len = step - prev_step
            
            remain = d - step
            loop_count = remain // cycle_len
            
            if loop_count > 0:
                step += cycle_len * loop_count
                
                visited = {} 
                continue

        visited[state] = step

        nx = x + dx[direction]
        ny = y + dy[direction]

        if (nx, ny) in obstacles:
            direction = (direction + 1) % 4
        else:
            x, y = nx, ny
            step += 1

    print(f"{x} {y}")