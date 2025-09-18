from collections import deque
import sys
input = sys.stdin.readline

maze_num = 1

while True:
    n = int(input().rstrip())
    if n == 0:
        break

    coords = list(map(int, input().rstrip().split()))
    start = tuple(coords[:n])
    end = tuple(coords[n:])

    graph = {}

    while True:
        line = input().rstrip()
        if line == "-1":
            break

        path_coords = list(map(int, line.split()))
        pos1 = tuple(path_coords[:n])
        pos2 = tuple(path_coords[n:])

        if pos1 not in graph:
            graph[pos1] = []
        if pos2 not in graph:
            graph[pos2] = []

        graph[pos1].append(pos2)
        graph[pos2].append(pos1)

    def can_reach(start, end, graph):
        if start == end:
            return True

        if start not in graph:
            return False

        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()

            if current == end:
                return True

            if current in graph:
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return False

    if can_reach(start, end, graph):
        print(f"Maze #{maze_num} can be travelled")
    else:
        print(f"Maze #{maze_num} cannot be travelled")

    maze_num += 1